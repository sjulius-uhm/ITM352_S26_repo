# FIN-ANALYTIX

Company Financial Data Web Scraper and Analysis Tool

## Project Description

FIN-ANALYTIX is a Flask-based financial analysis web application that retrieves company financial data using the `yfinance` library and allows users to analyze and compare companies through an interactive web interface.

The application supports:

* single-company financial analysis
* multi-company comparison
* financial ratio calculations
* financial health scoring
* chart visualizations
* CSV and Excel exports
* user authentication
* saved analysis history and downloads

The goal of the project is to provide a structured and user-friendly tool for exploring company financial performance and comparing businesses using real financial statement data.

---

## Team Members and Roles

### Samantha

* Data retrieval and cleaning
* Testing and debugging
* Documentation
* Error handling improvements

### Paul

* Financial ratio calculations
* Financial scoring system
* Company categorization and comparison logic

### Justin

* Flask integration
* Frontend templates and UI
* Authentication system
* Export/download system

---

## Main Features

* User login and registration system
* Dashboard with recent analyses
* Single-company financial analysis
* Multi-company comparison tool
* Financial ratio calculations
* Financial health scoring system
* Company categorization
* Financial chart generation
* CSV export
* Excel export with formatting
* Downloads Center
* User-specific history tracking
* Invalid ticker handling and input cleaning

---

## Technologies Used

* Python
* Flask
* Pandas
* Matplotlib
* yfinance
* openpyxl
* HTML/CSS
* JSON

---

## Installation Instructions

Install the required Python packages:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```
python app.py
```

Then open the following address in your web browser:

```
http://127.0.0.1:5001
```

---

## How to Use the Application

### 1. Register/Login

Create an account or log in using the login page.

### 2. Dashboard

The dashboard displays:

* total analyses
* rank summaries
* recent analyses
* quick analysis form

### 3. Analyze a Company

Go to the **Analyze** page and enter a ticker symbol such as:

```
AAPL
MSFT
TSLA
```

The app will:

* retrieve financial data
* calculate ratios
* generate a score
* categorize the company
* generate charts
* allow CSV/Excel downloads

### 4. Compare Companies

Go to the **Industry Compare** page and enter 2–5 ticker symbols separated by commas:

```
AAPL, MSFT, GOOGL
```

The app will:

* compare companies side-by-side
* calculate averages
* generate comparison charts
* handle invalid tickers safely

### 5. Downloads Center

Saved CSV and Excel files can be downloaded from the Downloads Center.

---

## Software Architecture Overview

The application is divided into three main layers:

### Data Retrieval Layer

Handles:

* ticker cleaning
* financial statement retrieval
* data cleaning
* financial dictionary creation

### Financial Analysis Layer

Handles:

* ratio calculations
* scoring
* categorization
* comparisons
* chart generation

### Web Application Layer

Handles:

* Flask routes
* templates
* authentication
* downloads
* exports
* dashboard functionality

---

## Testing Summary

The application was tested using:

* valid ticker symbols
* invalid ticker symbols
* single-company analysis
* multi-company comparison
* login/register functionality
* downloads and exports
* mixed valid/invalid comparisons

Financial values were cross-checked with Yahoo Finance and SEC EDGAR.

Detailed testing information is available in:

```
testing_results.md
```

---

## AI Usage

AI tools were used to assist with:

* Flask debugging
* Jinja template debugging
* function organization
* documentation improvements
* HTML/CSS cleanup
* testing ideas
* financial ratio suggestions

All AI-generated suggestions were reviewed, tested, modified, and integrated by the team.