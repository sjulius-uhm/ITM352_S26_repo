# Write a code that creates a list with a variety of different values
# Include control logic (if, elif, else) that will print different messages whether the list contains fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. 
# Test your code on lists with several different lengths.

def describe_list(values):
    if len(values) < 5:
        print(f"Length {len(values)}: fewer than 5 elements.")
    elif 5 <= len(values) <= 10:
        print(f"Length {len(values)}: between 5 and 10 elements.")
    else:
        print(f"Length {len(values)}: more than 10 elements.")


my_list = [1, "hello", 3.14, True, None]
describe_list(my_list)

# Create a list of lists with test cases for each possible condition. 
# Use this list to test that the code behaves as expected.

test_cases = [
    [1, 2],  # Fewer than 5 elements
    ["a", "b", "c", "d"],  # Fewer than 5 elements
    [1, 2, 3, 4, 5],  # Exactly 5 elements
    [1, "x", 3.14, False, None, "y", 7],  # Between 5 and 10 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Exactly 10 elements
    list(range(12))  # More than 10 elements
]
for test in test_cases:
    describe_list(test)

