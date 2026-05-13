# Final Project Requirements Document

## FIN-ANALYTIX: Company Financial Data Web Scraper and Analysis Tool

---

# 1. Original and Creative Project

## Requirement

The project must demonstrate originality, creativity, and not simply copy an existing tutorial or AI-generated application.

## How We Satisfied This Requirement

Our project combines multiple features into one integrated financial analysis web application:

* company financial data retrieval
* ratio analysis
* financial scoring
* multi-company comparison
* chart generation
* user authentication
* CSV/Excel exporting
* downloads management
* user-specific dashboards
* personal user watchlist
* dashboard watchlist widget
* market sentiment analysis from recent company news

While tutorials and examples exist for individual parts (such as Flask dashboards, web scraping, or CSV exports), we did not find a single tutorial or existing application that implemented our full feature set together in the same workflow.

We also tested whether AI could fully implement the project. AI could generate small sections such as basic Flask routes or isolated functions, but it could not successfully create the entire integrated system with:

* consistent data structures
* working user authentication
* comparison workflows
* organized file exports
* ranking systems
* chart generation
* downloads management
* robust error handling

The project required significant debugging, restructuring, testing, and integration work by the team.

---

# 2. Application of Technical Course Concepts

## Inputs and Outputs

### Requirement

The program must include user input and meaningful output.

### How We Satisfied This Requirement

Users interact with the application through HTML forms and navigation pages.

Inputs include:

* ticker symbols
* multiple comparison tickers
* usernames/passwords
* custom export filenames
* watchlist actions

Outputs include:

* financial data tables
* calculated ratios
* financial health scores
* company categories
* comparison tables
* charts
* downloadable CSV/Excel files
* personal watchlist tables
* dashboard watchlist summaries
* sentiment labels and positive/negative headline indicators

---

## Logic and Functions

### Requirement

The project must be divided into logical functions and codeable chunks.

### How We Satisfied This Requirement

The application is organized into separate functions for:

* data retrieval
* data cleaning
* calculations
* categorization
* comparisons
* chart generation
* exports
* authentication
* file management

Examples:

* `get_statement_data()`
* `build_clean_financial_dict()`
* `calculate_ratios()`
* `categorize_company()`
* `calculate_score()`
* `compare_companies()`
* `save_outputs()`

---

## Data Structures

### Requirement

The project must use appropriate data structures.

### How We Satisfied This Requirement

The project uses:

* dictionaries for company data and ratios
* lists for multi-company comparisons
* Pandas DataFrames for structured exports
* JSON files for user accounts and history tracking
* user watchlists stored in `users.json`

Examples:

* `financial_data` dictionary
* `ratios` dictionary
* `data_list`
* `users.json`
* `analysis_history.json`

---

## Error Handling

### Requirement

The project must include robust error handling.

### How We Satisfied This Requirement

The application handles:

* invalid ticker symbols
* missing financial data
* divide-by-zero calculations
* empty form inputs
* unauthorized page access
* missing files during download

Examples:

* invalid comparison tickers are skipped instead of crashing the application
* `safe_value()` prevents crashes caused by missing values
* login protection prevents unauthorized access to routes

---

## Class Topics

### Requirement

The project must demonstrate most major course concepts.

### How We Satisfied This Requirement

| Course Topic                | How It Was Used                                  |
| --------------------------- | ------------------------------------------------ |
| Data Analysis               | Financial ratio calculations and company scoring |
| Pandas                      | Data cleaning and CSV/Excel export               |
| Statistical Charts          | Matplotlib financial charts                      |
| File I/O                    | JSON, CSV, and Excel file handling               |
| Web Scraping/Data Retrieval | yfinance financial retrieval                     |
| Web Pages                   | HTML/Jinja templates                             |
| Web Application/GUI         | Flask application and routes                     |

---

## Stretch Goal

### Requirement

Research and use at least one non-trivial concept not learned in class.

### How We Satisfied This Requirement

We researched and implemented:

* `yfinance` for financial data retrieval
* Flask session-based authentication
* styled Excel exports using `openpyxl`
* dynamic chart generation with matplotlib
* user-specific history and downloads management
* TextBlob sentiment analysis on recent company news headlines
* personal watchlist tracking connected to user accounts

These technologies required independent research outside of normal class examples.

---

# 3. MIS Project Management Practices

## Documentation

### Requirement

Provide clear documentation.

### How We Satisfied This Requirement

We created:

* a project proposal
* technical requirements documentation
* testing documentation
* setup/use instructions
* code comments explaining major sections
* software architecture explanations

---

## Testing Plan

### Requirement

Create a testing plan showing the application works correctly.

### How We Satisfied This Requirement

Completed tests included:

* valid ticker analysis
* invalid ticker handling
* multi-company comparisons
* mixed valid/invalid comparisons
* login and registration
* dashboard tracking
* downloads functionality
* CSV/Excel export testing

Financial values were cross-checked with Yahoo Finance and SEC EDGAR for accuracy.

---

# 4. Polished Final Product

## Requirement

The project should be organized, user-friendly, robust, and polished.

## How We Satisfied This Requirement

The application includes:

* organized navigation
* dashboard summaries
* comparison tools
* financial charts
* color-coded tables
* downloadable exports
* user-specific analysis history
* clean page layouts
* consistent styling
* robust error handling
* personal watchlist page
* dashboard watchlist widget
* Add to Watchlist workflow through company analysis

The final application is fully functional and supports multiple financial analysis workflows through a user-friendly web interface.

---

# Conclusion

FIN-ANALYTIX satisfies the technical, organizational, and project management requirements of the course while demonstrating integration of multiple technologies, financial analysis concepts, structured web application development, and collaborative software design.