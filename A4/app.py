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
    """Cleans the ticker input from the user."""
    ticker = ticker.strip().upper()
    return ticker


def get_statement_data(ticker):
    """Gets financial statement data from Yahoo Finance using yfinance."""
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
    """Replaces missing values with 0."""
    if statement is None or statement.empty:
        return pd.DataFrame()
    return statement.fillna(0)


def get_value(statement, row_name):
    """Gets one value from a financial statement by row name."""
    try:
        return statement.loc[row_name].iloc[0]
    except Exception:
        return 0


def build_clean_financial_dict(ticker):
    """Builds a clean financial dictionary for one company."""
    ticker = clean_ticker(ticker)
    balance_sheet, income_statement, cash_flow = get_statement_data(ticker)

    if balance_sheet is None or balance_sheet.empty:
        return None

    balance_sheet = clean_statement(balance_sheet)
    income_statement = clean_statement(income_statement)
    cash_flow = clean_statement(cash_flow)

    financial_data = {
        "ticker": ticker,
        "total_assets": get_value(balance_sheet, "Total Assets"),
        "total_liabilities": get_value(balance_sheet, "Total Liabilities Net Minority Interest"),
        "stockholders_equity": get_value(balance_sheet, "Stockholders Equity"),
        "current_assets": get_value(balance_sheet, "Current Assets"),
        "current_liabilities": get_value(balance_sheet, "Current Liabilities"),
        "total_revenue": get_value(income_statement, "Total Revenue"),
        "net_income": get_value(income_statement, "Net Income"),
        "gross_profit": get_value(income_statement, "Gross Profit"),
        "operating_income": get_value(income_statement, "Operating Income"),
        "operating_cash_flow": get_value(cash_flow, "Operating Cash Flow"),
        "free_cash_flow": get_value(cash_flow, "Free Cash Flow"),
    }
    return financial_data


def get_financial_data(ticker_symbol):
    """Main company data dictionary for templates."""
    ticker_symbol = clean_ticker(ticker_symbol)
    raw = build_clean_financial_dict(ticker_symbol)

    if raw is None:
        raise ValueError("No company data found for ticker: " + ticker_symbol)

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
    """Calculate financial ratios from the company data dictionary."""
    net_income = safe_value(data.get("Net Income"))
    revenue = safe_value(data.get("Total Revenue"))
    total_cash = safe_value(data.get("Total Cash"))
    total_debt = safe_value(data.get("Total Debt"))
    market_cap = safe_value(data.get("Market Cap"))

    ratios = {}

    if net_income is not None and revenue and revenue != 0:
        ratios["Net Profit Margin"] = net_income / revenue
    else:
        ratios["Net Profit Margin"] = None

    if total_cash is not None and total_debt and total_debt != 0:
        ratios["Cash to Debt Ratio"] = total_cash / total_debt
    else:
        ratios["Cash to Debt Ratio"] = None

    if market_cap is not None and revenue and revenue != 0:
        ratios["Market Cap to Revenue"] = market_cap / revenue
    else:
        ratios["Market Cap to Revenue"] = None

    ratios["Debt to Equity"] = safe_value(data.get("Debt to Equity"))
    ratios["Trailing PE"] = safe_value(data.get("Trailing PE"))
    ratios["Return on Equity"] = safe_value(data.get("Return on Equity"))

    return ratios


def calculate_score(data, ratios):
    """Calculates a professional financial health score (0-100)."""
    WEIGHTS = {
        "profitability": 0.40,
        "liquidity_debt": 0.30,
        "efficiency": 0.20,
        "valuation": 0.10
    }

    scores = {"profitability": 50, "liquidity_debt": 50, "efficiency": 50, "valuation": 50}

    # Profitability
    margin = safe_value(ratios.get("Net Profit Margin"))
    if margin is not None:
        if margin > 0.20: scores["profitability"] = 100
        elif margin > 0.10: scores["profitability"] = 80
        elif margin < 0: scores["profitability"] = 20
        else: scores["profitability"] = 40

    # Liquidity & Debt
    d_e = safe_value(ratios.get("Debt to Equity"))
    cash_debt = safe_value(ratios.get("Cash to Debt Ratio"))
    debt_score = 50
    if d_e is not None:
        if d_e < 50: debt_score = 100
        elif d_e > 200: debt_score = 20
    if cash_debt is not None and cash_debt > 1.2:
        debt_score = min(100, debt_score + 20)
    scores["liquidity_debt"] = debt_score

    # Efficiency
    roe = safe_value(ratios.get("Return on Equity"))
    if roe is not None:
        if roe > 0.20: scores["efficiency"] = 100
        elif roe < 0.05: scores["efficiency"] = 30

    # Valuation
    pe = safe_value(ratios.get("Trailing PE"))
    if pe is not None:
        if 0 < pe < 15: scores["valuation"] = 100
        elif pe > 50: scores["valuation"] = 30

    final_score = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS)
    return round(final_score)


def categorize_company(data, ratios):
    """Categorize a company based on its data and ratios."""
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


def get_rank_folder(score):
    """Returns the rank folder name based on the score."""
    for folder_name, info in RANK_FOLDERS.items():
        if info["min"] <= score <= info["max"]:
            return folder_name
    return "Risky"


def compare_companies(data_list):
    """Compares financial data between multiple companies."""
    if not data_list or len(data_list) < 2:
        return None

    comparison_metrics = ["Current Price", "Market Cap", "Total Revenue", "Gross Profits", "Net Income", "Total Cash", "Total Debt", "Book Value"]
    ratio_metrics = ["Net Profit Margin", "Cash to Debt Ratio", "Market Cap to Revenue", "Debt to Equity", "Trailing PE", "Return on Equity"]

    comparison = {}
    for metric in comparison_metrics + ratio_metrics:
        row = {}
        values = []
        for entry in data_list:
            ticker = entry["data"]["Ticker"]
            val = safe_value(entry["data"].get(metric) if metric in comparison_metrics else entry["ratios"].get(metric))
            row[ticker] = val
            if val is not None: values.append(val)
        row["Average"] = sum(values) / len(values) if values else None
        comparison[metric] = row
    return comparison


def make_chart(ticker_symbol, data, ratios):
    """Creates a simple bar chart of selected financial values."""
    chart_values = {
        "Revenue": safe_value(data.get("Total Revenue")),
        "Net Income": safe_value(data.get("Net Income")),
        "Cash": safe_value(data.get("Total Cash")),
        "Debt": safe_value(data.get("Total Debt")),
    }
    chart_values = {k: v for k, v in chart_values.items() if v is not None}
    if not chart_values: return None

    plt.figure(figsize=(8, 5))
    plt.bar(chart_values.keys(), chart_values.values(), color=['#27ae60', '#27ae60', '#27ae60', '#e74c3c'])
    plt.title(f"Financials for {ticker_symbol}")
    plt.tight_layout()
    
    chart_filename = f"{ticker_symbol}_financial_chart.png"
    plt.savefig(os.path.join(CHART_FOLDER, chart_filename))
    plt.close()
    return f"charts/{chart_filename}"


def make_comparison_chart(data_list):
    """Creates a grouped bar chart comparing multiple companies."""
    tickers = [entry["data"]["Ticker"] for entry in data_list]
    metrics = ["Total Revenue", "Net Income", "Total Cash", "Total Debt"]

    plt.figure(figsize=(10, 6))
    x = np.arange(len(tickers))
    width = 0.2
    for i, metric in enumerate(metrics):
        vals = [safe_value(e["data"].get(metric)) or 0 for e in data_list]
        plt.bar(x + i * width, vals, width, label=metric)

    plt.xticks(x + width * 1.5, tickers)
    plt.legend()
    plt.tight_layout()
    
    chart_filename = "comparison_chart.png"
    plt.savefig(os.path.join(CHART_FOLDER, chart_filename))
    plt.close()
    return f"charts/{chart_filename}"


def save_outputs(ticker_symbol, data, ratios, category, score, custom_filename=None):
    """Saves results to CSV and Excel."""
    rank_folder = get_rank_folder(score)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = custom_filename.replace(" ", "_") if custom_filename else f"{ticker_symbol}_analysis_{timestamp}"

    csv_path = os.path.join(OUTPUT_FOLDER, rank_folder, f"{base_name}.csv")
    excel_path = os.path.join(OUTPUT_FOLDER, rank_folder, f"{base_name}.xlsx")

    rows = [{"Section": "Data", "Metric": k, "Value": v} for k, v in data.items()] + \
           [{"Section": "Ratios", "Metric": k, "Value": v} for k, v in ratios.items()]
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)
    df.to_excel(excel_path, index=False)

    history = load_history()
    history.append({
        "username": session.get("username"),
        "ticker": ticker_symbol,
        "category": category,
        "score": score,
        "rank_folder": rank_folder,
        "csv_file": f"{rank_folder}/{base_name}.csv",
        "excel_file": f"{rank_folder}/{base_name}.xlsx",
        "timestamp": timestamp,
    })
    save_history(history)
    return f"{rank_folder}/{base_name}.csv", f"{rank_folder}/{base_name}.xlsx"


def get_value_class(key, value):
    """CSS class for highlighting."""
    if value == "Not available": return "neutral"
    try:
        num = float(str(value).replace("$", "").replace(",", "").replace("%", ""))
        if key in ["Net Income", "Net Profit Margin"] and num < 0: return "negative"
        if key == "Total Debt" and num > 0: return "negative"
        return "positive" if num > 0 else "neutral"
    except: return "neutral"


# ---- Flask Routes ----


@app.route("/", methods=["GET"])
@login_required
def home():
    username = session.get("username")
    all_history = load_history()
    history = [e for e in all_history if e.get("username") == username]
    recent = history[-5:][::-1]
    rank_counts = {"High Rank": 0, "Stable": 0, "Risky": 0}
    for e in history:
        f = e.get("rank_folder")
        if f in rank_counts: rank_counts[f] += 1
    return render_template("dashboard.html", recent=recent, rank_counts=rank_counts, total=len(history))


@app.route("/analyze", methods=["GET", "POST"])
@login_required
def analyze():
    if request.method == "POST":
        ticker_symbol = request.form.get("ticker", "").upper().strip()
        custom_filename = request.form.get("custom_filename", "").strip()
        try:
            data = get_financial_data(ticker_symbol)
            ratios = calculate_ratios(data)
            category = categorize_company(data, ratios)
            score = calculate_score(data, ratios)
            chart_file = make_chart(ticker_symbol, data, ratios)
            csv_file, excel_file = save_outputs(ticker_symbol, data, ratios, category, score, custom_filename)

            display_data = {k: {"value": format_currency(v) if k in ["Net Income", "Total Revenue"] else v, "class": get_value_class(k, v)} for k, v in data.items()}
            display_ratios = {k: {"value": format_number(v), "class": get_value_class(k, v)} for k, v in ratios.items()}

            return render_template("results.html", ticker=ticker_symbol, data=display_data, ratios=display_ratios, category=category, score=score, chart_file=chart_file, csv_file=csv_file, excel_file=excel_file)
        except Exception as e:
            return render_template("analyze.html", error=str(e))
    return render_template("analyze.html")


@app.route("/compare", methods=["GET", "POST"])
@login_required
def compare():
    if request.method == "POST":
        tickers_raw = request.form.get("tickers", "")
        ticker_list = [t.strip().upper() for t in tickers_raw.replace(";", ",").split(",") if t.strip()]
        
        if len(ticker_list) < 2:
            return render_template("compare.html", error="Enter at least 2 tickers.")

        data_list = []
        for ticker in ticker_list:
            try:
                d = get_financial_data(ticker)
                r = calculate_ratios(d)
                data_list.append({"data": d, "ratios": r, "category": categorize_company(d, r), "score": calculate_score(d, r)})
            except: continue

        if len(data_list) < 2:
            return render_template("compare.html", error="Valid data for 2 companies not found.")

        comparison = compare_companies(data_list)
        chart_file = make_comparison_chart(data_list)
        
        display_comparison = {}
        for metric, row in comparison.items():
            display_comparison[metric] = {ticker: {"value": format_number(val), "class": get_value_class(metric, val)} for ticker, val in row.items()}

        return render_template("compare_results.html", comparison=display_comparison, tickers=[d["data"]["Ticker"] for d in data_list], chart_file=chart_file)
    
    return render_template("compare.html")

# ---- Downloads and File Serving Routes ----

@app.route("/downloads")
@login_required
def downloads():
    """Downloads Center page showing saved analyses for the logged-in user only."""
    username = session.get("username")
    all_history = load_history()
    
    # Filter history for current user
    user_history = [entry for entry in all_history if entry.get("username") == username]

    files_by_rank = {}
    for folder_name, info in RANK_FOLDERS.items():
        files = []
        for entry in user_history:
            if entry.get("rank_folder") == folder_name:
                # Add CSV entry
                if entry.get("csv_file"):
                    files.append({
                        "name": os.path.basename(entry["csv_file"]),
                        "path": entry["csv_file"],
                        "ext": ".csv"
                    })
                # Add Excel entry
                if entry.get("excel_file"):
                    files.append({
                        "name": os.path.basename(entry["excel_file"]),
                        "path": entry["excel_file"],
                        "ext": ".xlsx"
                    })
        
        files_by_rank[folder_name] = {
            "label": info["label"],
            "files": files
        }

    return render_template("downloads.html", files_by_rank=files_by_rank)

@app.route("/get-file/<path:filepath>")
@login_required
def get_file(filepath):
    """
    Actually serves the file from the outputs folder.
    The <path:filepath> allows for subfolders like 'Stable/filename.csv'.
    """
    # Security check: Ensure the user is only accessing the outputs folder
    return send_file(os.path.join(OUTPUT_FOLDER, filepath), as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)