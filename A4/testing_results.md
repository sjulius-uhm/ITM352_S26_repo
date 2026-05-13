# Testing Results

FIN-ANALYTIX: Company Financial Data Web Scraper and Analysis Tool

---

# Testing Overview

The application was tested throughout development to verify:

* financial data accuracy
* user input handling
* comparison functionality
* downloads and exports
* authentication features
* robustness against invalid input and missing data

Financial values were cross-checked against Yahoo Finance and SEC EDGAR whenever possible.

---

# Test Cases and Results

| Test ID | Feature Tested                 | Test Input                     | Expected Result                              | Actual Result                                | Status |
| ------- | ------------------------------ | ------------------------------ | -------------------------------------------- | -------------------------------------------- | ------ |
| T1      | User Registration              | New username/password          | Account created successfully                 | Account created and stored in `users.json`   | PASS   |
| T2      | Login System                   | Valid username/password        | User logs in successfully                    | Login successful and redirected to dashboard | PASS   |
| T3      | Invalid Login                  | Incorrect password             | Error message displayed                      | Error displayed without crashing             | PASS   |
| T4      | Protected Routes               | Access dashboard without login | Redirect to login page                       | Redirected correctly                         | PASS   |
| T5      | Single Company Analysis        | `AAPL`                         | Financial data retrieved and displayed       | Data displayed correctly                     | PASS   |
| T6      | Invalid Ticker Analysis        | `ABCDE`                        | Error message shown                          | Invalid ticker handled safely                | PASS   |
| T7      | Ticker Cleaning                | `aApL`                         | Input cleaned to `AAPL`                      | Company analyzed successfully                | PASS   |
| T8      | Multi-Company Comparison       | `AAPL, MSFT, GOOGL`            | Side-by-side comparison displayed            | Comparison generated correctly               | PASS   |
| T9      | Mixed Valid/Invalid Comparison | `AAPL, MSFT, BADDDD`           | Valid companies compared and invalid skipped | Invalid ticker skipped successfully          | PASS   |
| T10     | Comparison Input Limit         | More than 5 tickers            | Error message displayed                      | Error displayed correctly                    | PASS   |
| T11     | Ratio Calculations             | Valid financial data           | Ratios calculated correctly                  | Ratios displayed correctly                   | PASS   |
| T12     | Financial Scoring              | Valid company data             | Score generated between 0–100                | Score generated correctly                    | PASS   |
| T13     | Company Categorization         | Different financial profiles   | Company categorized correctly                | Categories displayed correctly               | PASS   |
| T14     | CSV Export                     | Analyze company and export     | CSV file created                             | CSV downloaded successfully                  | PASS   |
| T15     | Excel Export                   | Analyze company and export     | Excel file created                           | Excel downloaded successfully                | PASS   |
| T16     | Excel Formatting               | Positive/negative values       | Color formatting applied                     | Excel styling worked correctly               | PASS   |
| T17     | Downloads Center               | Open Downloads Center          | User files displayed                         | Files displayed correctly                    | PASS   |
| T18     | User-Specific History          | Multiple user accounts         | Users only see their own history             | Dashboard filtered correctly                 | PASS   |
| T19     | Chart Generation               | Analyze company                | Financial chart created                      | Chart displayed correctly                    | PASS   |
| T20     | Comparison Chart               | Compare companies              | Comparison chart generated                   | Chart displayed correctly                    | PASS   |
| T21     | Missing Financial Values       | Company with incomplete data   | Application continues safely                 | Missing values handled correctly             | PASS   |
| T22     | Divide-by-Zero Protection      | Revenue/debt edge cases        | No crash during calculations                 | Handled safely using checks                  | PASS   |
| T23     | File Downloads                 | Download CSV/Excel             | Files download correctly                     | Files downloaded successfully                | PASS   |
| T24     | Navigation Links               | Move between pages             | Navigation works correctly                   | All links functional                         | PASS   |

---

# Error Handling Tests

## Invalid Tickers

The application was tested with invalid ticker symbols such as:

```
ABCDE
FAKE
XXXXXX
```

Result:

* The application did not crash.
* Invalid tickers displayed error messages.
* Invalid comparison tickers were skipped while valid companies still compared successfully.

---

## Missing or Incomplete Financial Data

Some companies may not contain all financial statement values.

Result:

* Missing values were safely converted using `safe_value()`.
* Ratio calculations avoided divide-by-zero errors.
* The application continued running without crashing.

---

# Data Accuracy Verification

Financial values retrieved from `yfinance` were manually compared against:

* Yahoo Finance
* SEC EDGAR

Tested companies included:

```
AAPL
MSFT
TSLA
NVDA
MCD
```

Result:

* Major financial values closely matched public financial data sources.

---

# Final Testing Conclusion

The FIN-ANALYTIX application successfully passed all major functional tests.

The final application:

* retrieves and analyzes financial data correctly
* handles invalid input safely
* generates comparisons and charts
* exports CSV and Excel files
* supports user authentication
* organizes user-specific history and downloads
* remains stable during normal and error-case testing

The project was tested for both functionality and robustness to ensure a polished final product.
