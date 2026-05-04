# Hey Samantha and Paul - Read This Before You Start

This is the web app for our financial scraper project. The Flask routes, templates, login system, charts, and file exports are all done.

**Paul's data retrieval code is already integrated.** His functions (`get_statement_data`, `build_clean_financial_dict`, etc.) are in `app.py` and working. There's a bridge function called `get_financial_data()` that takes Paul's output and maps it to the keys the web UI expects.

What's still missing is **Samantha's three analysis functions** inside `app.py`. Right now they are placeholder stubs that raise `NotImplementedError`. Once you fill them in, everything will work.

---

## Paul - Your Code is Already In

Your functions are integrated and working:
- `clean_ticker(ticker)`
- `get_statement_data(ticker)`
- `clean_statement(statement)`
- `get_value(statement, row_name)`
- `build_clean_financial_dict(ticker)`
- `get_multiple_companies_data(ticker_list)`

The bridge function `get_financial_data()` calls your `build_clean_financial_dict()` and maps your lowercase keys (like `total_revenue`) to the Title Case keys the web UI uses (like `Total Revenue`). It also pulls some extra fields from `yfinance`'s `company.info` (like Sector, Industry, Current Price, etc.) that your DataFrame approach doesn't cover.

**You don't need to change anything unless you want to.** If you do make changes to your functions, just make sure `build_clean_financial_dict()` still returns the same keys.

---

## Samantha - Analysis

You need to fill in **three functions** in `app.py`. They all receive the dictionary that `get_financial_data()` returns. Search for `NotImplementedError` in the file to find them.

The data dictionary you'll receive has these keys:

```
"Ticker"              - string, the ticker symbol
"Company Name"        - string
"Sector"              - string
"Industry"            - string
"Current Price"       - float
"Market Cap"          - float
"Total Revenue"       - float
"Gross Profits"       - float
"Net Income"          - float
"Total Cash"          - float
"Total Debt"          - float (this is total liabilities)
"Book Value"          - float
"Profit Margin"       - float (decimal like 0.25 not 25%)
"Return on Equity"    - float (decimal like 0.15 not 15%)
"Debt to Equity"      - float
"Trailing PE"         - float
"Forward PE"          - float
"Recommendation"      - string
"Total Assets"        - float  (from Paul's functions)
"Total Liabilities"   - float  (from Paul's functions)
"Stockholders Equity" - float  (from Paul's functions)
"Current Assets"      - float  (from Paul's functions)
"Current Liabilities" - float  (from Paul's functions)
"Operating Income"    - float  (from Paul's functions)
"Operating Cash Flow" - float  (from Paul's functions)
"Free Cash Flow"      - float  (from Paul's functions)
```

### `calculate_ratios(data)`
- Takes the company data dictionary
- Calculate and return a dictionary with these exact keys:

```
"Net Profit Margin"     - Net Income / Total Revenue
"Cash to Debt Ratio"    - Total Cash / Total Debt
"Market Cap to Revenue" - Market Cap / Total Revenue
"Debt to Equity"        - just pass through from data
"Trailing PE"           - just pass through from data
"Return on Equity"      - just pass through from data
```

- Use `safe_value()` before doing math (it handles None/missing values)
- If you can't calculate a ratio (missing data or divide by zero), set it to `None`
- You also have access to Paul's extra fields (Total Assets, Operating Cash Flow, Free Cash Flow, etc.) if you want to add more ratios

### `categorize_company(data, ratios)`
- Takes the data dictionary and the ratios dictionary you calculated
- Return **one** of these exact strings:
  - `"Losing Company"` - if net income is negative
  - `"Growth / Strong Profit Company"` - if profit margin is above 15%
  - `"Possible Value Company"` - if PE ratio is between 0 and 20
  - `"Neutral / Needs More Review"` - default if nothing else matches

### `calculate_score(data, ratios)`
- Takes the data dictionary and ratios dictionary
- Return a number from 0 to 100
- This score decides which folder the analysis gets saved to:
  - **80-100** = HIGH_RANK folder
  - **50-79** = STABLE folder
  - **0-49** = WATCHLIST folder
- Start at 50 and add or subtract points based on how good or bad the numbers are
- Use `max(0, min(100, score))` at the end to keep it in range

### Quick start example
```python
def calculate_ratios(data):
    revenue = safe_value(data.get("Total Revenue"))
    net_income = safe_value(data.get("Net Income"))

    ratios = {}
    if revenue and net_income is not None and revenue != 0:
        ratios["Net Profit Margin"] = net_income / revenue
    else:
        ratios["Net Profit Margin"] = None

    # ... fill in the rest ...
    return ratios
```

---

## How to Test

1. Install packages: `pip install -r requirements.txt`
2. Run: `python app.py`
3. Open `http://127.0.0.1:5000` in your browser
4. Create an account and try analyzing a ticker like AAPL

If your functions return the right keys, everything else (charts, tables, downloads, color coding) will just work automatically.

---

## Important

- **Do not rename the function names or the dictionary keys.** The routes and templates use these exact names.
- Use `safe_value()` when pulling values from dictionaries. It's already in the file and handles None/missing data.
- If you have questions look at the `notes.md` file for a description of the whole app.
