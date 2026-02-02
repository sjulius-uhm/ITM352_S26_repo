# Manipulate a list in various ways
# Samantha Julius
# Date: Feb. 1, 2026

# PART A: Using .append() and .insert() methods
print("=== PART A: Using .append() and .insert() ===")
responseValues = [5, 7, 3, 8]
responseValues.append(0)
print("After appending 0:", responseValues)

responseValues.insert(2, 6)
print("After inserting 6 at index 2:", responseValues)

# PART B: Using list slicing and + operator
print("\n=== PART B: Using list slicing and + operator ===")
responseValues = [5, 7, 3, 8]
responseValues = responseValues + [0]
print("After appending 0:", responseValues)

responseValues = responseValues[:2] + [6] + responseValues[2:]
print("After inserting 6 at index 2:", responseValues)