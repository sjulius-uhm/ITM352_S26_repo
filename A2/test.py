# I used ChatGPT to help organize testing documentation and create ideas for automated testing output.

import io
from contextlib import redirect_stdout
from unittest.mock import patch


from A2.dashboard import (
    load_csv,
    display_initial_rows,
    total_sales_by_region_order_type,
    average_sales_by_region_state_sale_type,
    sales_by_customer_type_order_type_state,
    total_sales_quantity_price_region_product,
    total_sales_quantity_price_customer_type,
    max_min_sales_price_by_category,
    unique_employees_by_region,
    create_custom_pivot_table
)

def run_tests():
    output_file = "test_results.txt"

    with open(output_file, "w") as f:
        with redirect_stdout(f):
            print("=== Dashboard Test Results ===\n")

            # Load data
            df = load_csv("sales_data.csv")

            print("\n--- Test 1: Preview first 5 rows ---")
            with patch("builtins.input", return_value="5"):
                display_initial_rows(df)

            print("\n--- Test 2: Preview all rows ---")
            with patch("builtins.input", return_value="all"):
                display_initial_rows(df)

            print("\n--- Test 3: Skip preview ---")
            with patch("builtins.input", return_value=""):
                display_initial_rows(df)

            print("\n--- Test 4: Total sales by region and order_type ---")
            total_sales_by_region_order_type(df)

            print("\n--- Test 5: Average sales by region with state and sale type ---")
            average_sales_by_region_state_sale_type(df)

            print("\n--- Test 6: Sales by customer type and order type by state ---")
            sales_by_customer_type_order_type_state(df)

            print("\n--- Test 7: Total sales quantity and price by region and product ---")
            total_sales_quantity_price_region_product(df)

            print("\n--- Test 8: Total sales quantity and price by customer type ---")
            total_sales_quantity_price_customer_type(df)

            print("\n--- Test 9: Max and min sales price by category ---")
            max_min_sales_price_by_category(df)

            print("\n--- Test 10: Number of unique employees by region ---")
            unique_employees_by_region(df)

            print("\n--- Test 11: Custom pivot table ---")
            custom_inputs = ["1", "1", "1", "1"]  
            # rows = employee_name
            # columns = order_type
            # values = quantity
            # aggfunc = sum

            with patch("builtins.input", side_effect=custom_inputs):
                create_custom_pivot_table(df)

            print("\n=== End of Tests ===")

    print(f"Testing complete. Results saved to {output_file}")

if __name__ == "__main__":
    run_tests()