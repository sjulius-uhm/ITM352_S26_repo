# Company Financial Data Web Scraper and Analysis Tool

This is a Flask starter application for the Assignment 4 project proposal.

## What the app does

- Lets the user enter a company ticker symbol
- Retrieves company financial data using `yfinance`
- Calculates simple financial ratios
- Categorizes the company using basic criteria
- Creates a simple financial chart
- Exports results to CSV and Excel
- Displays results through a Flask website

## Install requirements

```bash
pip install -r requirements.txt
```

## Run the app

```bash
python app.py
```

Then open this in a browser:

```text
http://127.0.0.1:5000
```

For phone testing on the same Wi-Fi network, the app already uses:

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

Use your computer's local IP address with port 5000.

## Example ticker symbols

- AAPL
- MSFT
- TSLA
- NVDA
- KO
- MCD

## Notes for class submission

This version uses `yfinance` instead of directly scraping Yahoo Finance HTML with BeautifulSoup. This is usually more stable because financial websites often change their page structure or block scraping. If the instructor requires BeautifulSoup, this app can be modified to add a scraping function later.

Before submitting, review the code and make sure you understand it. You can also simplify or expand the calculations depending on the final project requirements.
