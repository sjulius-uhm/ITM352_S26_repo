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

        # Income Statement
        "total_revenue": get_value(income_statement, "Total Revenue"),
        "net_income": get_value(income_statement, "Net Income"),
        "gross_profit": get_value(income_statement, "Gross Profit"),

        # Cash Flow
        "operating_cash_flow": get_value(cash_flow, "Operating Cash Flow"),
        "free_cash_flow": get_value(cash_flow, "Free Cash Flow")
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


def print_financial_data(financial_data):
    """
    Prints the cleaned financial data in a readable format for testing.
    """
    print("\nCleaned Financial Data")
    print("----------------------")

    for key, value in financial_data.items():
        print(key, ":", value)


def main():
    """
    Test function for multiple companies.
    Allows user to input several tickers separated by commas.
    """
    ticker_input = input("Enter company tickers separated by commas: ")

    ticker_list = ticker_input.split(",")

    company_data_list = get_multiple_companies_data(ticker_list)

    print("\nAll Company Data")
    print("----------------")

    if len(company_data_list) == 0:
        print("No valid company data found.")
    else:
        for company_data in company_data_list:
            print_financial_data(company_data)


if __name__ == "__main__":
    main()