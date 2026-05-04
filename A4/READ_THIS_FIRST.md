# Hey Samantha and Paul - Read This Before You Start

This is the web app for our financial scraper project. The Flask routes, templates, login system, charts, and file exports are all done. What's missing is **your functions** inside `app.py`.

Right now if you run the app it will crash when you try to analyze a company because your functions are placeholder stubs that say `NotImplementedError`. Once you fill them in, everything will work.

---

## Paul - Data Retrieval

You need to fill in **two functions** in `app.py`:

### `get_financial_data(ticker_symbol)`
- Takes a ticker symbol string like `"AAPL"` or `"MSFT"`
- Use `yfinance` to pull the company's financial info
- Return a dictionary with these exact keys (the rest of the app depends on them):

```
"Ticker"           - string, the ticker symbol
"Company Name"     - string
"Sector"           - string
"Industry"         - string
"Current Price"    - float
"Market Cap"       - float
"Total Revenue"    - float
"Gross Profits"    - float
"Net Income"       - float
"Total Cash"       - float
"Total Debt"       - float
"Book Value"       - float
"Profit Margin"    - float (decimal like 0.25 not 25%)
"Return on Equity" - float (decimal like 0.15 not 15%)
"Debt to Equity"   - float
"Trailing PE"      - float
"Forward PE"       - float
"Recommendation"   - string
```

- If the ticker doesn't exist, raise a `ValueError`
- Call `clean_data(data)` on your dictionary before returning it

### `clean_data(data)`
- Takes the raw dictionary from `get_financial_data()`
- Make sure numeric fields are actual floats (not strings or weird values)
- Make sure string fields are stripped of extra whitespace
- Replace bad values with `None` so the app doesn't crash
- Return the cleaned dictionary

### Quick start example
```python
def get_financial_data(ticker_symbol):
    ticker_symbol = ticker_symbol.upper().strip()
    company = yf.Ticker(ticker_symbol)
    info = company.info

    if not info or info.get("currentPrice") is None:
        raise ValueError("No data found for that ticker symbol.")

    data = {
        "Ticker": ticker_symbol,
        "Company Name": info.get("longName"),
        # ... fill in the rest using info.get("keyName") ...
    }
    return clean_data(data)
```

---

## Samantha - Analysis

You need to fill in **three functions** in `app.py`. They all receive the dictionary that Paul's `get_financial_data()` returns.

### `calculate_ratios(data)`
- Takes the company data dictionary
- Calculate and return a dictionary with these exact keys:

```
"Net Profit Margin"    - Net Income / Total Revenue
"Cash to Debt Ratio"   - Total Cash / Total Debt
"Market Cap to Revenue" - Market Cap / Total Revenue
"Debt to Equity"       - just pass through from data
"Trailing PE"          - just pass through from data
"Return on Equity"     - just pass through from data
```

- Use `safe_value()` before doing math (it handles None/missing values)
- If you can't calculate a ratio (missing data or divide by zero), set it to `None`

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
