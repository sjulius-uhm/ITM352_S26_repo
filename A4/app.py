"""
Company Financial Data Web Scraper and Analysis Tool

This Flask application lets users log in, analyze company financial data, compare multiple companies, generate charts, and export results to CSV/Excel.

AI Use Note:
AI was used to help organize the Flask app structure, debug errors, improve function comments, and support data retrieval/analysis logic. All code was reviewed, tested, and edited by the team.
"""

from flask import Flask, render_template, request, send_file, redirect, url_for, session
from functools import wraps
import os
import json
from datetime import datetime

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Lets matplotlib save charts without opening a window
import matplotlib.pyplot as plt
import numpy as np

try:
    import yfinance as yf
except ImportError:
    yf = None


app = Flask(__name__)
app.secret_key = "fin-analytix-secret-key-2026"

USERS_FILE = "users.json"
OUTPUT_FOLDER = "outputs"
CHART_FOLDER = os.path.join("static", "charts")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(CHART_FOLDER, exist_ok=True)


# Rank folders for organizing saved analyses
RANK_FOLDERS = {
    "High Rank": {"label": "High Rank (Score 80-100)", "min": 80, "max": 100},
    "Stable": {"label": "Stable (Score 50-79)", "min": 50, "max": 79},    
    "Risky": {"label": "Risky (Score 0-49)", "min": 0, "max": 49},
}


# Create rank subfolders inside outputs
for folder_name in RANK_FOLDERS:
    os.makedirs(os.path.join(OUTPUT_FOLDER, folder_name), exist_ok=True)


# File to persist analysis history
HISTORY_FILE = os.path.join(OUTPUT_FOLDER, "analysis_history.json")


def load_history():
    """Load analysis history from disk."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(history):
    """Save analysis history to disk."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def load_users():
    """Load user accounts from disk."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users):
    """Save user accounts to disk."""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def login_required(f):
    """Decorator that redirects to login page if user is not signed in."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

def add_to_watchlist(username, ticker):
    """Adds a ticker to the user's specific watchlist."""
    users = load_users()
    if username in users:
        # Check if user data is a dict (new format) or string (old password-only format)
        if isinstance(users[username], str):
            users[username] = {"password": users[username], "watchlist": []}
        
        if "watchlist" not in users[username]:
            users[username]["watchlist"] = []

        if ticker not in users[username]["watchlist"]:
            users[username]["watchlist"].append(ticker)
            save_users(users)
            return True
    return False

def get_top_movers():
    """Fetches high-activity tickers for the dashboard widget."""
    movers = []
    # Major indices/tech for the widget
    sample_tickers = ["AAPL", "TSLA", "NVDA", "MSFT", "AMD"]
    for t in sample_tickers:
        try:
            ticker = yf.Ticker(t)
            hist = ticker.history(period="2d")
            if len(hist) >= 2:
                prev_close = hist['Close'].iloc[-2]
                curr_close = hist['Close'].iloc[-1]
                change = ((curr_close - prev_close) / prev_close) * 100
                movers.append({"ticker": t, "price": round(curr_close, 2), "change": round(change, 2)})
        except: continue
    return sorted(movers, key=lambda x: abs(x['change']), reverse=True)[:5]
@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page."""
    if "username" in session:
        return redirect(url_for("home"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            error = "Please fill in both fields."
        else:
            users = load_users()
            if username in users and users[username] == password:
                session["username"] = username
                return redirect(url_for("home"))
            else:
                error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Registration page."""
    if "username" in session:
        return redirect(url_for("home"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        confirm = request.form.get("confirm", "").strip()

        if not username or not password:
            error = "Please fill in all fields."
        elif len(password) < 4:
            error = "Password must be at least 4 characters."
        elif password != confirm:
            error = "Passwords do not match."
        else:
            users = load_users()
            if username in users:
                error = "That username is already taken."
            else:
                users[username] = password
                save_users(users)
                session["username"] = username
                return redirect(url_for("home"))

    return render_template("register.html", error=error)


@app.route("/logout")
def logout():
    """Log the user out."""
    session.pop("username", None)
    return redirect(url_for("login"))


def safe_value(value):
    """Converts missing or invalid values into None so the app does not crash."""
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    return value


def format_currency(value):
    """Formats large financial numbers for display on the webpage."""
    value = safe_value(value)
    if value is None:
        return "Not available"
    try:
        return "${:,.0f}".format(float(value))
    except (ValueError, TypeError):
        return "Not available"


def format_number(value):
    """Formats ratios and percentages for display."""
    value = safe_value(value)
    if value is None:
        return "Not available"
    try:
        return "{:,.2f}".format(float(value))
    except (ValueError, TypeError):
        return "Not available"


def format_percent(value):
    """Formats a decimal ratio as a percentage string."""
    value = safe_value(value)
    if value is None:
        return "Not available"
    try:
        return "{:.2f}%".format(float(value) * 100)
    except (ValueError, TypeError):
        return "Not available"


# ---- Data Retrieval Functions ----


def clean_ticker(ticker):
    """
    Cleans the ticker input from the user.
    Example: " aapl " becomes "AAPL"
    """
    ticker = ticker.strip()
    ticker = ticker.upper()
    return ticker


def get_statement_data(ticker):
    """
    Gets financial statement data from Yahoo Finance using yfinance.
    Returns balance sheet, income statement, and cash flow statement.
    """
    try:
        company = yf.Ticker(ticker)

        balance_sheet = company.balance_sheet
        income_statement = company.financials
        cash_flow = company.cashflow

        return balance_sheet, income_statement, cash_flow

    except Exception as error:
        print("Error getting financial data for", ticker, ":", error)
        return None, None, None


def clean_statement(statement):
    """
    Cleans one financial statement.
    Replaces missing values with 0.
    """
    if statement is None or statement.empty:
        return pd.DataFrame()

    statement = statement.fillna(0)
    return statement


def get_value(statement, row_name):
    """
    Gets one value from a financial statement by row name.
    Uses the most recent column of data.
    """
    try:
        value = statement.loc[row_name].iloc[0]
        return value

    except Exception:
        return 0


def build_clean_financial_dict(ticker):
    """
    Builds a clean financial dictionary for one company.
    This dictionary can be used for calculations, comparisons, and display.
    """
    ticker = clean_ticker(ticker)

    balance_sheet, income_statement, cash_flow = get_statement_data(ticker)

    if balance_sheet is None or balance_sheet.empty:
        print("Invalid ticker or no data found for:", ticker)
        return None

    balance_sheet = clean_statement(balance_sheet)
    income_statement = clean_statement(income_statement)
    cash_flow = clean_statement(cash_flow)

    financial_data = {
        "ticker": ticker,

        # Balance Sheet
        "total_assets": get_value(balance_sheet, "Total Assets"),
        "total_liabilities": get_value(balance_sheet, "Total Liabilities Net Minority Interest"),
        "stockholders_equity": get_value(balance_sheet, "Stockholders Equity"),
        "current_assets": get_value(balance_sheet, "Current Assets"),
        "current_liabilities": get_value(balance_sheet, "Current Liabilities"),

        # Income Statement
        "total_revenue": get_value(income_statement, "Total Revenue"),
        "net_income": get_value(income_statement, "Net Income"),
        "gross_profit": get_value(income_statement, "Gross Profit"),
        "operating_income": get_value(income_statement, "Operating Income"),

        # Cash Flow
        "operating_cash_flow": get_value(cash_flow, "Operating Cash Flow"),
        "free_cash_flow": get_value(cash_flow, "Free Cash Flow"),
    }

    return financial_data


def get_multiple_companies_data(ticker_list):
    """
    Gets cleaned financial data for multiple companies.
    Used for company comparisons.
    """
    company_data_list = []

    for ticker in ticker_list:
        ticker = clean_ticker(ticker)

        if ticker == "":
            continue

        print("Getting data for:", ticker)

        financial_data = build_clean_financial_dict(ticker)

        if financial_data is not None:
            company_data_list.append(financial_data)
        else:
            print("Skipping invalid ticker:", ticker)

    return company_data_list



# ---- Data Mapping Function ----


def get_financial_data(ticker_symbol):
    """
    Creates the main company data dictionary used by the app.

    This function calls build_clean_financial_dict() to retrieve financial
    statement values, then adds extra company information from yfinance so
    the templates have one consistent dictionary to use.
    """

    ticker_symbol = clean_ticker(ticker_symbol)
    raw = build_clean_financial_dict(ticker_symbol)

    if raw is None:
        raise ValueError("No company data was found. Check the ticker symbol and try again.")

    company = yf.Ticker(ticker_symbol)
    info = company.info

    data = {
        "Ticker": ticker_symbol,
        "Company Name": info.get("longName", ticker_symbol),
        "Sector": info.get("sector", "N/A"),
        "Industry": info.get("industry", "N/A"),
        "Current Price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "Market Cap": info.get("marketCap"),
        "Total Revenue": raw.get("total_revenue"),
        "Gross Profits": raw.get("gross_profit"),
        "Net Income": raw.get("net_income"),
        "Total Cash": info.get("totalCash"),
        "Total Debt": raw.get("total_liabilities"),
        "Book Value": info.get("bookValue"),
        "Profit Margin": info.get("profitMargins"),
        "Return on Equity": info.get("returnOnEquity"),
        "Debt to Equity": info.get("debtToEquity"),
        "Trailing PE": info.get("trailingPE"),
        "Forward PE": info.get("forwardPE"),
        "Recommendation": info.get("recommendationKey"),
        "Total Assets": raw.get("total_assets"),
        "Total Liabilities": raw.get("total_liabilities"),
        "Stockholders Equity": raw.get("stockholders_equity"),
        "Current Assets": raw.get("current_assets"),
        "Current Liabilities": raw.get("current_liabilities"),
        "Operating Income": raw.get("operating_income"),
        "Operating Cash Flow": raw.get("operating_cash_flow"),
        "Free Cash Flow": raw.get("free_cash_flow"),
    }

    return data


# ---- Financial Analysis Functions ----


def calculate_ratios(data):
    """
    Calculate financial ratios from the company data dictionary.
    """
    # Extract values safely
    net_income = safe_value(data.get("Net Income"))
    revenue = safe_value(data.get("Total Revenue"))
    total_cash = safe_value(data.get("Total Cash"))
    total_debt = safe_value(data.get("Total Debt"))
    market_cap = safe_value(data.get("Market Cap"))

    ratios = {}

    # Net Profit Margin: (Net Income / Total Revenue)
    if net_income is not None and revenue and revenue != 0:
        ratios["Net Profit Margin"] = net_income / revenue
    else:
        ratios["Net Profit Margin"] = None

    # Cash to Debt Ratio: (Total Cash / Total Debt)
    if total_cash is not None and total_debt and total_debt != 0:
        ratios["Cash to Debt Ratio"] = total_cash / total_debt
    else:
        ratios["Cash to Debt Ratio"] = None

    # Market Cap to Revenue: (Market Cap / Total Revenue)
    if market_cap is not None and revenue and revenue != 0:
        ratios["Market Cap to Revenue"] = market_cap / revenue
    else:
        ratios["Market Cap to Revenue"] = None

    # Directly map existing ratios from data
    ratios["Debt to Equity"] = safe_value(data.get("Debt to Equity"))
    ratios["Trailing PE"] = safe_value(data.get("Trailing PE"))
    ratios["Return on Equity"] = safe_value(data.get("Return on Equity"))

    return ratios


def categorize_company(data, ratios):
    """
    Categorize a company based on its data and ratios.
    """
    net_income = safe_value(data.get("Net Income"))
    profit_margin = safe_value(ratios.get("Net Profit Margin"))
    pe_ratio = safe_value(ratios.get("Trailing PE"))

    if net_income is not None and net_income < 0:
        return "Losing Company"
    
    if profit_margin is not None and profit_margin > 0.15:
        return "Growth / Strong Profit Company"
    
    if pe_ratio is not None and 0 < pe_ratio <= 20:
        return "Possible Value Company"

    return "Neutral / Needs More Review"


def calculate_score(data, ratios):
    """
    Calculate a financial health score from 0-100.
    """
    score = 50  # Start at Neutral
    
    # 1. Profitability (Up to +15 or -15)
    margin = safe_value(ratios.get("Net Profit Margin"))
    if margin is not None:
        if margin > 0.20: score += 15
        elif margin > 0.10: score += 5
        elif margin < 0: score -= 15

    # 2. Return on Equity (Up to +15)
    roe = safe_value(ratios.get("Return on Equity"))
    if roe is not None:
        if roe > 0.15: score += 15
        elif roe > 0.08: score += 5

    # 3. Debt Management (Up to +10 or -20)
    d_e = safe_value(ratios.get("Debt to Equity"))
    if d_e is not None:
        if d_e < 50: score += 10    # Low debt
        elif d_e > 150: score -= 20  # High debt

    # 4. Cash Position (Up to +10)
    cash_debt = safe_value(ratios.get("Cash to Debt Ratio"))
    if cash_debt is not None and cash_debt > 1.0:
        score += 10 # Can pay off all debt with cash

    # 5. Valuation (Up to +10 or -10)
    pe = safe_value(ratios.get("Trailing PE"))
    if pe is not None:
        if 0 < pe < 15: score += 10
        elif pe > 50: score -= 10

    # Clamp final score to 0-100 range
    return max(0, min(100, score))


def get_rank_folder(score):
    """Returns the rank folder name based on the score."""
    for folder_name, info in RANK_FOLDERS.items():
        if info["min"] <= score <= info["max"]:
            return folder_name
    return "Risky"


def compare_companies(data_list):
    """
    Compares financial data between multiple companies.

    Takes a list of company data dictionaries and produces a comparison
    showing each company's metrics side by side, along with averages
    and which company ranks best/worst in each metric.
    """
    if not data_list or len(data_list) < 2:
        return None

    comparison_metrics = [
        "Current Price", "Market Cap", "Total Revenue", "Gross Profits",
        "Net Income", "Total Cash", "Total Debt", "Book Value",
    ]
    ratio_metrics = [
        "Net Profit Margin", "Cash to Debt Ratio", "Market Cap to Revenue",
        "Debt to Equity", "Trailing PE", "Return on Equity",
    ]

    # Build comparison table
    comparison = {}
    for metric in comparison_metrics:
        row = {}
        values = []
        for entry in data_list:
            val = safe_value(entry["data"].get(metric))
            ticker = entry["data"]["Ticker"]
            row[ticker] = val
            if val is not None:
                values.append(val)
        row["Average"] = sum(values) / len(values) if values else None
        comparison[metric] = row

    for metric in ratio_metrics:
        row = {}
        values = []
        for entry in data_list:
            val = safe_value(entry["ratios"].get(metric))
            ticker = entry["data"]["Ticker"]
            row[ticker] = val
            if val is not None:
                values.append(val)
        row["Average"] = sum(values) / len(values) if values else None
        comparison[metric] = row

    return comparison


def make_chart(ticker_symbol, data, ratios):
    """
    Creates a simple bar chart of selected financial values.

    The chart is saved into the static folder so Flask can display it on the results page.
    """
    chart_values = {
        "Revenue": safe_value(data.get("Total Revenue")),
        "Net Income": safe_value(data.get("Net Income")),
        "Cash": safe_value(data.get("Total Cash")),
        "Debt": safe_value(data.get("Total Debt")),
    }

    # Remove values that are missing so the chart only shows available data.
    chart_values = {key: value for key, value in chart_values.items() if value is not None}

    if not chart_values:
        return None

    colors = []
    for key, val in chart_values.items():
        if key == "Debt":
            colors.append("#e74c3c")
        elif val >= 0:
            colors.append("#27ae60")
        else:
            colors.append("#e74c3c")

    plt.figure(figsize=(8, 5))
    plt.bar(chart_values.keys(), chart_values.values(), color=colors)
    plt.title(f"Selected Financial Data for {ticker_symbol}")

    # Format y-axis to show billions/millions instead of raw numbers
    ax = plt.gca()
    max_val = max(abs(v) for v in chart_values.values())
    if max_val >= 1_000_000_000:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x/1_000_000_000:.1f}B"))
        plt.ylabel("Amount (Billions USD)")
    elif max_val >= 1_000_000:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x/1_000_000:.1f}M"))
        plt.ylabel("Amount (Millions USD)")
    else:
        plt.ylabel("Amount (USD)")

    plt.xticks(rotation=20)
    plt.tight_layout()

    chart_filename = f"{ticker_symbol}_financial_chart.png"
    chart_path = os.path.join(CHART_FOLDER, chart_filename)
    plt.savefig(chart_path)
    plt.close()

    return f"charts/{chart_filename}"


def make_comparison_chart(data_list):
    """
    Creates a grouped bar chart comparing multiple companies.
    """
    tickers = [entry["data"]["Ticker"] for entry in data_list]
    metrics = ["Total Revenue", "Net Income", "Total Cash", "Total Debt"]

    values_by_metric = {}
    for metric in metrics:
        vals = []
        for entry in data_list:
            v = safe_value(entry["data"].get(metric))
            vals.append(v if v is not None else 0)
        values_by_metric[metric] = vals

    x = np.arange(len(tickers))
    width = 0.2
    fig, ax = plt.subplots(figsize=(10, 6))

    for i, (metric, vals) in enumerate(values_by_metric.items()):
        ax.bar(x + i * width, vals, width, label=metric)

    ax.set_xlabel("Company")
    ax.set_title("Company Comparison")
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(tickers)
    ax.legend()

    # Format y-axis to show billions/millions
    all_vals = [v for vals in values_by_metric.values() for v in vals if v != 0]
    if all_vals:
        max_val = max(abs(v) for v in all_vals)
        if max_val >= 1_000_000_000:
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x/1_000_000_000:.1f}B"))
            ax.set_ylabel("Amount (Billions USD)")
        elif max_val >= 1_000_000:
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x/1_000_000:.1f}M"))
            ax.set_ylabel("Amount (Millions USD)")
        else:
            ax.set_ylabel("Amount (USD)")
    else:
        ax.set_ylabel("Amount (USD)")

    plt.tight_layout()

    chart_filename = "comparison_chart.png"
    chart_path = os.path.join(CHART_FOLDER, chart_filename)
    plt.savefig(chart_path)
    plt.close()

    return f"charts/{chart_filename}"


def save_outputs(ticker_symbol, data, ratios, category, score, custom_filename=None):
    """
    Saves the results to both CSV and Excel.

    This matches the proposal's export feature. The Excel file also includes basic
    color formatting to make stronger and weaker values easier to notice.
    Files are saved into rank-based subfolders.
    """
    rank_folder = get_rank_folder(score)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if custom_filename:
        base_name = custom_filename.replace(" ", "_")
    else:
        base_name = f"{ticker_symbol}_financial_analysis_{timestamp}"

    csv_filename = f"{base_name}.csv"
    excel_filename = f"{base_name}.xlsx"

    csv_path = os.path.join(OUTPUT_FOLDER, rank_folder, csv_filename)
    excel_path = os.path.join(OUTPUT_FOLDER, rank_folder, excel_filename)

    rows = []
    for key, value in data.items():
        rows.append({"Section": "Company Data", "Metric": key, "Value": value})
    for key, value in ratios.items():
        rows.append({"Section": "Calculated Ratios", "Metric": key, "Value": value})
    rows.append({"Section": "Category", "Metric": "Company Category", "Value": category})
    rows.append({"Section": "Score", "Metric": "Financial Health Score", "Value": score})

    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)

    # Create a styled Excel file with simple highlighting.
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Financial Analysis")
        worksheet = writer.sheets["Financial Analysis"]

        from openpyxl.styles import PatternFill, Font

        header_fill = PatternFill(start_color="D9EAF7", end_color="D9EAF7", fill_type="solid")
        positive_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        negative_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

        for cell in worksheet[1]:
            cell.fill = header_fill
            cell.font = Font(bold=True)

        for row in range(2, worksheet.max_row + 1):
            value_cell = worksheet.cell(row=row, column=3)
            try:
                value = float(value_cell.value)
                if value > 0:
                    value_cell.fill = positive_fill
                elif value < 0:
                    value_cell.fill = negative_fill
            except (TypeError, ValueError):
                pass

        worksheet.column_dimensions["A"].width = 22
        worksheet.column_dimensions["B"].width = 28
        worksheet.column_dimensions["C"].width = 24

    # Record to history
    history = load_history()
    history.append({
       "username": session.get("username"),
        "ticker": ticker_symbol,
        "company_name": data.get("Company Name", ticker_symbol),
        "category": category,
        "score": score,
        "rank_folder": rank_folder,
        "csv_file": f"{rank_folder}/{csv_filename}",
        "excel_file": f"{rank_folder}/{excel_filename}",
        "timestamp": timestamp,
    })
    save_history(history)

    return f"{rank_folder}/{csv_filename}", f"{rank_folder}/{excel_filename}"


def get_value_class(key, value):
    """
    Returns a CSS class name for color highlighting table cells.

    Green for positive/good values, red for negative/bad values.
    This implements the color highlighting from Milestone 3.
    """
    if value == "Not available":
        return "neutral"

    try:
        num = float(value.replace("$", "").replace(",", "").replace("%", ""))
    except (ValueError, TypeError, AttributeError):
        return "neutral"

    # Metrics where higher is better
    positive_metrics = [
        "Total Revenue", "Gross Profits", "Net Income", "Total Cash",
        "Book Value", "Current Price", "Market Cap",
        "Net Profit Margin", "Cash to Debt Ratio", "Return on Equity",
    ]
    # Metrics where lower is better
    negative_metrics = ["Total Debt", "Debt to Equity"]

    if key in positive_metrics:
        return "positive" if num > 0 else "negative"
    elif key in negative_metrics:
        return "negative" if num > 100 else "positive" if num >= 0 else "negative"
    elif key == "Trailing PE" or key == "Forward PE":
        if 0 < num < 25:
            return "positive"
        elif num > 40:
            return "negative"
        return "neutral"

    return "neutral"


# ---- Flask Routes ----
# These routes control the main pages and actions of the web application.
# Each route connects user actions from the website to the backend functions above.


# Dashboard route:
# Shows the logged-in user's recent analyses and summary counts and adds in the dashboard for watchlist
@app.route("/", methods=["GET"])
@login_required
def home():
    username = session.get("username")
    all_history = load_history()
    history = [e for e in all_history if e.get("username") == username]
    recent = history[-5:][::-1]
    
    # NEW: Fetch Top Movers for the dashboard widget
    movers = get_top_movers()
    
    rank_counts = {"High Rank": 0, "Stable": 0, "Risky": 0}
    for e in history:
        f = e.get("rank_folder")
        if f in rank_counts: rank_counts[f] += 1
    return render_template("dashboard.html", recent=recent, rank_counts=rank_counts, total=len(history), movers=movers)


# Analyze route:
# Lets the user enter one ticker, runs the full analysis, saves outputs,
# and displays the results page.
@app.route("/analyze", methods=["GET", "POST"])
@login_required
def analyze():
    """Page where users enter a company ticker symbol for analysis."""
    if request.method == "POST":
        ticker_symbol = request.form.get("ticker", "").upper().strip()
        if not ticker_symbol:
            return render_template("analyze.html", error="Please enter a ticker symbol.")

        custom_filename = request.form.get("custom_filename", "").strip()

        try:
            data = get_financial_data(ticker_symbol)
            ratios = calculate_ratios(data)
            category = categorize_company(data, ratios)
            score = calculate_score(data, ratios)
            chart_file = make_chart(ticker_symbol, data, ratios)
            csv_file, excel_file = save_outputs(
                ticker_symbol, data, ratios, category, score,
                custom_filename=custom_filename if custom_filename else None
            )

            # Build display-ready data with CSS classes for color highlighting
            display_data = {}
            for key, value in data.items():
                if key in ["Current Price", "Market Cap", "Total Revenue", "Gross Profits",
                           "Net Income", "Total Cash", "Total Debt", "Book Value"]:
                    formatted = format_currency(value)
                else:
                    formatted = value if value is not None else "Not available"
                display_data[key] = {
                    "value": formatted,
                    "class": get_value_class(key, formatted),
                }

            display_ratios = {}
            for key, value in ratios.items():
                formatted = format_number(value)
                display_ratios[key] = {
                    "value": formatted,
                    "class": get_value_class(key, formatted),
                }

            return render_template(
                "results.html",
                ticker=ticker_symbol,
                data=display_data,
                ratios=display_ratios,
                category=category,
                score=score,
                rank_folder=get_rank_folder(score),
                chart_file=chart_file,
                csv_file=csv_file,
                excel_file=excel_file,
            )
        except Exception as error:
            return render_template("analyze.html", error=str(error))

    return render_template("analyze.html")


# Compare route:
# Lets the user enter multiple tickers and compares valid companies side by side.
# Invalid tickers are skipped so the rest of the comparison can still run.
@app.route("/compare", methods=["GET", "POST"])
@login_required
def compare():
    """Industry Compare page for comparing multiple companies side by side."""
    if request.method == "POST":
        tickers_raw = request.form.get("tickers", "")
        ticker_list = [t.strip().upper() for t in tickers_raw.replace(";", ",").split(",") if t.strip()]

        if len(ticker_list) < 2:
            return render_template("compare.html", error="Please enter at least 2 ticker symbols separated by commas.")

        if len(ticker_list) > 5:
            return render_template("compare.html", error="Please enter no more than 5 ticker symbols.")

        data_list = []
        invalid_tickers = []

        for ticker in ticker_list:
            try:
                data = get_financial_data(ticker)
                ratios = calculate_ratios(data)
                category = categorize_company(data, ratios)
                score = calculate_score(data, ratios)

                data_list.append({
                    "data": data,
                    "ratios": ratios,
                    "category": category,
                    "score": score,
                })

            except Exception:
                invalid_tickers.append(ticker)

        if len(data_list) < 2:
            return render_template(
                "compare.html",
                error="Please enter at least 2 valid ticker symbols."
            )

        comparison = compare_companies(data_list)
        chart_file = make_comparison_chart(data_list)

        currency_metrics = [
            "Current Price", "Market Cap", "Total Revenue", "Gross Profits",
            "Net Income", "Total Cash", "Total Debt", "Book Value",
        ]

        display_comparison = {}
        for metric, row in comparison.items():
            display_row = {}
            for col, val in row.items():
                if metric in currency_metrics:
                    formatted = format_currency(val)
                else:
                    formatted = format_number(val)

                display_row[col] = {
                    "value": formatted,
                    "class": get_value_class(metric, formatted),
                }

            display_comparison[metric] = display_row

        tickers = [entry["data"]["Ticker"] for entry in data_list]
        categories = {entry["data"]["Ticker"]: entry["category"] for entry in data_list}
        scores = {entry["data"]["Ticker"]: entry["score"] for entry in data_list}

        warning = None
        if len(invalid_tickers) > 0:
            warning = "Skipped invalid ticker(s): " + ", ".join(invalid_tickers)

        return render_template(
            "compare_results.html",
            tickers=tickers,
            comparison=display_comparison,
            categories=categories,
            scores=scores,
            chart_file=chart_file,
            warning=warning,
        )

    return render_template("compare.html")


# Downloads route:
# Shows saved CSV and Excel files for the logged-in user only.
@app.route("/downloads")
@login_required
def downloads():
    """Downloads Center page showing saved analyses for the logged-in user only."""

    username = session.get("username")
    history = [
        entry for entry in load_history()
        if entry.get("username") == username
    ]

    files_by_rank = {}

    for folder_name, info in RANK_FOLDERS.items():
        files = []

        for entry in history:
            if entry.get("rank_folder") == folder_name:
                files.append({
                    "name": os.path.basename(entry.get("csv_file", "")),
                    "path": entry.get("csv_file", ""),
                    "size": "",
                    "ext": ".csv",
                })

                files.append({
                    "name": os.path.basename(entry.get("excel_file", "")),
                    "path": entry.get("excel_file", ""),
                    "size": "",
                    "ext": ".xlsx",
                })

        files_by_rank[folder_name] = {
            "label": info["label"],
            "files": files,
        }

    return render_template("downloads.html", files_by_rank=files_by_rank)


# File download route:
# Sends a selected CSV or Excel file to the user's browser.
@app.route("/download/<path:filename>")
@login_required
def download_file(filename):
    # Build full absolute path
    file_path = os.path.join(os.getcwd(), OUTPUT_FOLDER, filename)

    # Check if file exists
    if not os.path.exists(file_path):
        return f"Error: File not found on server: {file_path}", 404

    # Force browser download
    return send_file(
        file_path,
        as_attachment=True,
        download_name=os.path.basename(file_path)
    )




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
