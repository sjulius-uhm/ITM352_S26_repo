# Project Notes - Company Financial Data Web Scraper and Analysis Tool

## Team Members
- Samantha - Data retrieval, cleaning, testing, and documentation
- Paul - Financial analysis calculations, scoring, and comparisons
- Justin - Flask integration, frontend templates, authentication, and exports

---
## Main Features

- User login and registration system
- Single-company financial analysis
- Multi-company comparison tool
- Financial ratio calculations and scoring
- CSV and Excel export generation
- Rank-based file organization
- Downloads Center with saved analyses
- Financial chart visualizations
- Invalid ticker handling and input cleaning


## Software Architecture

The project is divided into three main sections:

### 1. Data Retrieval Layer
Handles retrieving and cleaning financial statement data using the yfinance library. These functions standardize company data into a consistent dictionary format that the rest of the application can use.

Main functions:
- clean_ticker()
- get_statement_data()
- clean_statement()
- get_value()
- build_clean_financial_dict()

### 2. Financial Analysis Layer
Handles ratio calculations, company categorization, scoring, comparisons, and chart generation.

Main functions:
- calculate_ratios()
- categorize_company()
- calculate_score()
- compare_companies()
- make_chart()
- make_comparison_chart()

### 3. Web Application Layer
Handles the Flask routes, user authentication, templates, downloads, and frontend integration.

Main sections:
- Login/register system
- Dashboard
- Analyze page
- Compare page
- Downloads Center
- CSV/Excel export system

---
## File Descriptions and How They Were Created

### app.py
This is the main application file that runs everything. We built it using Flask as the web framework. It handles all the routes (pages) for the app and contains the functions for pulling financial data, doing calculations, making charts, and saving files.

- **Data retrieval (Samantha):** We wrote functions to pull company financial data using the yfinance library. The `get_financial_data()` function takes a ticker symbol, connects to Yahoo Finance, and returns a dictionary of financial values like revenue, net income, market cap, etc. We also wrote a `clean_data()` function to handle missing or bad values so the app doesn't crash.

- **Analysis (Paul):** We created functions to calculate financial ratios like net profit margin, cash to debt ratio, and market cap to revenue. The `categorize_company()` function sorts companies into categories (Growth, Value, Losing, Neutral) based on their numbers. We also built a scoring system from 0-100 that rates financial health, which determines if a company goes into HIGH_RANK, STABLE, or WATCHLIST folders.

- **Web interface and integration (Justin):** We set up all the Flask routes to connect the backend logic to the frontend pages. This includes the dashboard, analyze page, compare page, downloads page, and the login/register system. We also added file export functionality that saves results to CSV and Excel with color formatting, and organized saved files into rank-based folders.

- **User authentication:** We added a simple login and registration system using Flask sessions. User accounts are stored in a JSON file. All pages require the user to be signed in before they can access them.

- **Charts:** We used matplotlib to generate bar charts showing financial data. The y-axis labels automatically format numbers into millions or billions so the charts are easier to read.

### templates/base.html
This is the base template that all other pages extend. We created it to have a consistent layout across the whole app. It contains the navigation bar with links to Dashboard, Data Tables, Industry Compare, and Downloads Center. It also shows the logged-in username and a logout link.

### templates/login.html
The login page. We built this as a standalone page (not extending base.html) with a simple centered form for username and password. It shows error messages if the login fails and has a link to the registration page.

### templates/register.html
The registration page. Similar to the login page, it has fields for username, password, and confirm password. It validates that passwords match and are at least 4 characters long.

### templates/dashboard.html
The home page of the app. We built it to show an overview with stats cards (total analyses, high rank count, stable count, watchlist count), a quick analyze form, and a table of recent analyses with download links.

### templates/analyze.html
The main data entry page. We created a form where the user types in a ticker symbol and optionally a custom filename for exports. It also shows example ticker symbols as a reference.

### templates/results.html
The results page that shows up after analyzing a company. We designed it to display the company category, financial health score, a bar chart, and two tables side by side - one for raw company data and one for calculated ratios. Values are color coded green for positive and red for negative. Download buttons for CSV and Excel are included.

### templates/compare.html
The comparison input page. We made a form where users can type in 2-5 ticker symbols separated by commas to compare companies.

### templates/compare_results.html
Shows the comparison results with badges for each company (showing their score and category), a grouped bar chart comparing all companies, and a side-by-side data table with an average column.

### templates/downloads.html
The downloads center page. We organized it with collapsible folders for each rank category (HIGH_RANK, STABLE, WATCHLIST). Each folder shows the files inside it with their type (CSV or Excel) and a download button. We used JavaScript to toggle folders open and closed.

### templates/index.html
A simple redirect page. It just sends the user to the dashboard using JavaScript.

### static/style.css
The stylesheet for the entire app. We wrote basic CSS to style the navigation bar, forms, tables, cards, buttons, score badges, and color highlighting. We kept the design simple and functional.

### requirements.txt
Lists all the Python packages needed to run the app: Flask, pandas, matplotlib, yfinance, openpyxl, and numpy.

---
## Testing and Error Handling

The application was tested using both valid and invalid company ticker symbols.

Completed tests:
- Valid single-company analysis
- Valid multi-company comparison
- Invalid ticker handling
- Mixed valid/invalid ticker comparison
- User login and registration
- Downloads Center functionality
- CSV and Excel export generation
- User-specific dashboard and downloads history

Error handling features:
- Invalid tickers are skipped during comparisons
- Empty or malformed ticker input is cleaned automatically
- Missing financial values default safely to 0 or None
- Users cannot access protected pages without logging in
- The application prevents crashes caused by missing data or divide-by-zero calculations

---
## How to Open and Use the App

### Step 1: Install Python Packages
Open a terminal in the project folder and run:
```
pip install -r requirements.txt
```

### Step 2: Start the App
Run the following command:
```
python app.py
```
You should see output saying the server is running.

### Step 3: Open in Browser
Go to this address in your web browser:
```
http://127.0.0.1:5000
```

### Step 4: Create an Account
You will land on the login page. If you don't have an account yet, click "Register here" and create a username and password (password must be at least 4 characters).

### Step 5: Using the Dashboard
After signing in you will see the dashboard. It shows stats about your previous analyses and a quick search bar. You can also use the navigation bar at the top to go to different pages.

### Step 6: Analyze a Company
Go to "Data Tables" in the nav bar. Type a ticker symbol (like AAPL for Apple, MSFT for Microsoft, TSLA for Tesla) and click "Analyze Company." The results page will show the company's financial data, calculated ratios, a health score, a bar chart, and download buttons for CSV and Excel files.

### Step 7: Compare Companies
Go to "Industry Compare" in the nav bar. Type 2-5 ticker symbols separated by commas (like AAPL, MSFT, GOOGL) and click "Compare Companies." You will see a side-by-side comparison table, individual scores, and a grouped bar chart.

### Step 8: Download Files
Go to "Downloads Center" in the nav bar. Click on a rank folder (HIGH_RANK, STABLE, or WATCHLIST) to expand it and see saved analysis files. Click "Download" next to any file to save it to your computer.

### Step 9: Log Out
Click "Logout" in the top right corner of the navigation bar when you are done.

---
## AI Usage

AI tools were used to assist with:
- Debugging Flask and Jinja template errors
- Organizing Flask route structure
- Improving code readability and documentation
- Suggesting financial ratio formulas
- Assisting with HTML/CSS cleanup
- Generating testing ideas and project planning outlines

All AI-generated suggestions were reviewed, tested, modified, and integrated by the team.