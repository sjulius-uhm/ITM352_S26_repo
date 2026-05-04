# Samantha Julius
# May 3, 2026
# Data retrieval and cleaning for A4

import yfinance as yf
import pandas as pd


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
        print("Error getting financial data:", error)
        return None, None, None


def clean_statement(statement):
    """
    Cleans one financial statement.
    - Replaces missing values with 0
    - Converts values to numeric when possible
    """
    if statement is None:
        return pd.DataFrame()

    if statement.empty:
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
    ticker = clean_ticker(ticker)

    balance_sheet, income_statement, cash_flow = get_statement_data(ticker)

    # Check if data exists
    if balance_sheet is None or balance_sheet.empty:
        print("Invalid ticker or no data found.")
        return None

    balance_sheet = clean_statement(balance_sheet)
    income_statement = clean_statement(income_statement)
    cash_flow = clean_statement(cash_flow)

    financial_data = {
        "ticker": ticker,
        "total_assets": get_value(balance_sheet, "Total Assets"),
        "total_liabilities": get_value(balance_sheet, "Total Liabilities Net Minority Interest"),
        "stockholders_equity": get_value(balance_sheet, "Stockholders Equity"),
        "total_revenue": get_value(income_statement, "Total Revenue"),
        "net_income": get_value(income_statement, "Net Income"),
    }

    return financial_data


def print_financial_data(financial_data):
    """
    Prints the cleaned financial data in a readable format for testing.
    """
    print("\nCleaned Financial Data")
    print("----------------------")

    for key, value in financial_data.items():
        print(key, ":", value)


def main():
    ticker = input("Enter company ticker: ")

    financial_data = build_clean_financial_dict(ticker)

    if financial_data is None:
        print("No data available for this ticker.")
    else:
        print_financial_data(financial_data)


if __name__ == "__main__":
    main()