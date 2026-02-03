# Create loops to display all information in your dictionary.
# Samantha Julius
# Feb. 2, 2026

student_info = {
    "name": "Samantha Julius",
    "age": 20,
    "grade": "Junior",
    "subjects": ["Math", "Science", "History"],
    "gpa": 3.8
}

print("1. LOOPING THROUGH KEYS")
print("All keys in the dictionary:")
for key in student_info:
    print(f"  - {key}")
print()

print("All keys in the dictionary:")
for key in student_info:
    print(f"  - {key}")
print()

print("\n2. LOOPING THROUGH VALUES")
print("All values in the dictionary:")
for value in student_info.values():
    print(f"  - {value}")
print()

print("\n3. LOOPING THROUGH KEYS AND ACCESSING VALUES")
print("Key: Value pairs (using key to access value):")
for key in student_info:
    print(f"  {key}: {student_info[key]}")
print()

print("\n4. LOOPING THROUGH KEY-VALUE PAIRS (items method)")
print("Key: Value pairs (using items()):")
for key, value in student_info.items():
    print(f"  {key}: {value}")
print()

print("\n5. LOOPING WITH INDEX NUMBERS")
print("Numbered list of all information:")
for index, (key, value) in enumerate(student_info.items(), start=1):
    print(f"  {index}. {key}: {value}")
print()

print("\n6. FORMATTED DISPLAY")
print("Student Profile:")
for key, value in student_info.items():
    print(f"  {key.capitalize():12} : {value}")
print()

print("\n7. CONDITIONAL DISPLAY")
print("Display only string values:")
for key, value in student_info.items():
    if isinstance(value, str):
        print(f"  {key}: {value}")
print()

print("Display only numeric values:")
for key, value in student_info.items():
    if isinstance(value, (int, float)):
        print(f"  {key}: {value}")
print()

print("\n8. DISPLAY LIST ITEMS (subjects)")
print("Subjects enrolled:")
for index, subject in enumerate(student_info["subjects"], start=1):
    print(f"  {index}. {subject}")
print() 

print("COMPLETE STUDENT REPORT")
print(f"Name: {student_info ['name']}")
print(f"Age: {student_info['age']}")
print(f"Grade: {student_info['grade']}")
print(f"GPA: {student_info['gpa']}")
print(f"Email: {student_info['email'] if 'email' in student_info else 'N/A'}")
print(f"Subjects ({len(student_info['subjects'])} total):")
for i, subject in enumerate(student_info["subjects"], start=1):
    print(f"  {i}. {subject}")
print()
