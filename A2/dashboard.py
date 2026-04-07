import time
import pandas as pd
import numpy as np
import pyarrow

saved_results = {}

pd.set_option('display.max_columns', None)  

url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

df = pd.read_csv(url, engine='python')
df.to_csv("sales_data.csv", index=False)

# Create alternate dataset: Retail orders only
df_alt = df[df['order_type'] == 'Retail']
df_alt.to_csv("sales_data_alt.csv", index=False)

def choose_dataset():
    print("\nSelect sales data to load:")
    print("1. Main sales data")
    print("2. Alternate sales data (Retail only)")

    choice = input("Enter your choice (1-2): ").strip()

    if choice == "1":
        return "sales_data.csv"
    elif choice == "2":
        return "sales_data_alt.csv"
    else:
        print("Invalid choice. Defaulting to main sales data.")
        return "sales_data.csv"


def load_csv(filepath):
    print(f"Loading data from {filepath}...")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='python')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded succesfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Available columns: {df.columns.tolist()}")
        
        df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y', errors='coerce') 
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
        df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
        
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)
        
        if 'quantity' in df.columns and 'unit_price' in df.columns:
            df['sales'] = df['quantity'] * df['unit_price']
        
        required_columns = [
        'sales_region',
        'order_type',
        'customer_state',
        'customer_type',
        'produce_name',
        'product_category',
        'quantity',
        'unit_price',
        'employee_id',
        'order_date'
    ]

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")
            print(" Some analytics may not work as expected without these columns.")        
        else: 
            print("All required columns are present.")

        return df
    
    except Exception as e:
        raise SystemExit(f"Error loading CSV file: {e}")


def display_initial_rows(dataframe):
    print("\nEnter rows to display:")
    print(f"- Enter a number 1 to {len(dataframe)}")
    print("- To see all rows, enter 'all'")
    print("- To skip preview, press Enter")
    user_input = input("Your choice: ").strip().lower()

    if user_input == '':
        print("Skipping preview.")
        return
    elif user_input == 'all':
        print("Displaying all rows:")
        print(dataframe)
        saved_results["All rows preview"] = dataframe
    elif user_input.isdigit() and 1 <= int(user_input) <= len(dataframe):
        num_rows = int(user_input)
        result = dataframe.head(num_rows)
        print(f"Displaying first {num_rows} rows:")
        print(result)
        saved_results[f"First {num_rows} rows preview"] = result
    else:
        print("Invalid input. Please try again.")

def total_sales_by_region_order_type(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values='sales',
        index='sales_region',
        columns='order_type',
        aggfunc='sum',
        fill_value=0
    )
    print("\nTotal sales by region and order_type:")
    print(pivot_table)
    saved_results["Total sales by region and order_type"] = pivot_table

def average_sales_by_region_state_sale_type(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values='sales',
        index='sales_region',
        columns=['customer_state', 'order_type'],
        aggfunc='mean',
        fill_value=0
    )
    print("\nAverage sales by region with average sales by state and sale type:")
    print(pivot_table)
    saved_results["Average sales by region with average sales by state and sale type"] = pivot_table

def sales_by_customer_type_order_type_state(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values='sales',
        index=['customer_state', 'customer_type'],
        columns='order_type',
        aggfunc='sum',
        fill_value=0
    )
    print("\nSales by customer type and order type by state:")
    print(pivot_table)
    saved_results["Sales by customer type and order type by state"] = pivot_table


def total_sales_quantity_price_region_product(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values=['quantity', 'sales'],
        index=['sales_region', 'produce_name'],
        aggfunc='sum',
        fill_value=0
    )
    print("\nTotal sales quantity and price by region and product:")
    print(pivot_table)
    saved_results["Total sales quantity and price by region and product"] = pivot_table


def total_sales_quantity_price_customer_type(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values=['quantity', 'sales'],
        index=['order_type', 'customer_type'],
        aggfunc='sum',
        fill_value=0
    )
    print("\nTotal sales quantity and price by order type and customer type:")
    print(pivot_table)
    saved_results["Total sales quantity and price by order type and customer type"] = pivot_table

def max_min_sales_price_by_category(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values='sales',
        index='product_category',
        aggfunc=['max', 'min'],
        fill_value=0
    )
    print("\nMax and min sales price by category:")
    print(pivot_table)
    saved_results["Max and min sales price by category"] = pivot_table

def unique_employees_by_region(dataframe):
    pivot_table = pd.pivot_table(
        dataframe,
        values='employee_id',
        index='sales_region',
        aggfunc=pd.Series.nunique,
        fill_value=0
    )
    pivot_table.columns = ['Number of Unique Employees']
    print("\nNumber of unique employees by region:")
    print(pivot_table)
    saved_results["Number of unique employees by region"] = pivot_table

def create_custom_pivot_table(dataframe):
    row_options = ['employee_name', 'sales_region', 'product_category']
    column_options = ['order_type', 'customer_type']
    value_options = ['quantity', 'sales']
    agg_options = ['sum', 'mean', 'count']

    print("\nSelect rows:")
    for i, option in enumerate(row_options, start=1):
        print(f"{i}. {option}")
    row_input = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

    if row_input == "":
        print("You must choose at least one row field.")
        return

    try:
        rows = [row_options[int(i.strip()) - 1] for i in row_input.split(",")]
    except:
        print("Invalid row selection.")
        return

    print("\nSelect columns (optional):")
    for i, option in enumerate(column_options, start=1):
        print(f"{i}. {option}")
    col_input = input("Enter the number(s) of your choice(s), separated by commas (enter for no grouping): ").strip()

    try:
        if col_input == "":
            columns = []
        else:
            columns = [column_options[int(i.strip()) - 1] for i in col_input.split(",")]
    except:
        print("Invalid column selection.")
        return

    print("\nSelect values:")
    for i, option in enumerate(value_options, start=1):
        print(f"{i}. {option}")
    value_input = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

    if value_input == "":
        print("You must choose at least one value field.")
        return

    try:
        values = [value_options[int(i.strip()) - 1] for i in value_input.split(",")]
    except:
        print("Invalid value selection.")
        return

    print("\nSelect aggregation function:")
    for i, option in enumerate(agg_options, start=1):
        print(f"{i}. {option}")
    agg_input = input("Enter the number of your choice: ").strip()

    if not agg_input.isdigit() or not (1 <= int(agg_input) <= len(agg_options)):
        print("Invalid aggregation choice.")
        return

    aggfunc = agg_options[int(agg_input) - 1]

    pivot_table = pd.pivot_table(
        dataframe,
        index=rows,
        columns=columns if columns else None,
        values=values,
        aggfunc=aggfunc,
        fill_value=0
    )
    print("\nCustom Pivot Table:")
    print(pivot_table)

    custom_name = f"Custom Pivot Table {len([key for key in saved_results if 'Custom Pivot Table' in key]) + 1}"
    saved_results[custom_name] = pivot_table


def show_saved_results_list():
    print("\nStored analytics results:")
    if not saved_results:
        print("None yet.")
    else:
        for i, result_name in enumerate(saved_results.keys(), start=1):
            print(f"{i}. {result_name}")


def view_saved_result(dataframe):
    if not saved_results:
        print("\nNo stored results yet.")
        return
    print("\nSelect a stored result to view:")
    result_names = list(saved_results.keys())
    for i, name in enumerate(result_names, start=1):
        print(f"{i}. {name}")
    choice = input(f"Enter your choice (1-{len(result_names)}): ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return
    choice = int(choice)
    if 1 <= choice <= len(result_names):
        selected_name = result_names[choice - 1]
        print(f"\n{selected_name}:")
        print(saved_results[selected_name])
    else:
        print("Invalid choice.")


def display_all_saved_results(dataframe):
    print("\n--- All Stored Results ---")
    if not saved_results:
        print("No stored results yet.")
        return
    for result_name, result_table in saved_results.items():
        print(f"\n{result_name}:")
        print(result_table)


def exit_program(dataframe):
    print("Exiting the program. Goodbye!")
    exit(0)


def display_menu(dataframe):
    menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order_type", total_sales_by_region_order_type),
    ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_sale_type),
    ("Sales by customer type and order type by state", sales_by_customer_type_order_type_state),
    ("Total sales quantity and price by region and product", total_sales_quantity_price_region_product),
    ("Total sales quantity and price customer type", total_sales_quantity_price_customer_type),
    ("Max and min sales price of sales by category", max_min_sales_price_by_category),
    ("Number of unique employees by region", 
    unique_employees_by_region),
    ("Create a custom pivot table", create_custom_pivot_table),
    ("View a stored result", view_saved_result),
    ("Display all stored results", display_all_saved_results),
    ("Exit", exit_program) 
    )

    print("\n--- Sales Data Dashboard ---")
    for i, (description, _) in enumerate(menu_options, start=1):
        print(f"{i}. {description}")

    try:
        menu_len = len(menu_options)
        choice = int(input(f"Enter your choice (1-{menu_len}): "))
        if 1 <= choice <= menu_len:
            action = menu_options[choice - 1][1]
            action(dataframe)
        else:
            print("Invalid choice. Please enter a number corresponding to the options.")

    except ValueError:
        print("Invalid input. Please enter a number corresponding to the options.")


# filename = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
filename = "sales_data.csv"
sales_data = load_csv(filename)


# Run the main processing loop
def main():
    filename = choose_dataset()
    print(f"\nYou selected: {filename}\n")
    sales_data = load_csv(filename)

    while True:
        show_saved_results_list()
        display_menu(sales_data)

# Check if this is the main module being run
if __name__ == "__main__":
    main()