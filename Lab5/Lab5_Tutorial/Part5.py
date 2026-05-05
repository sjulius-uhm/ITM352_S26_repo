# Create a dictionary of multiple students, each with their own information dictionary.
# Samantha Julius
# Feb. 2, 2026

print("1. BASIC NESTED DICTIONARY")
students = {
    "Samantha": {
        "age": 20,
        "grade": "Junior",
        "gpa": 3.8
    },
    "Alice": {
        "age": 19,
        "grade": "Sophomore",
        "gpa": 3.9
    },
    "Bob": {
        "age": 21,
        "grade": "Senior",
        "gpa": 3.6
    }
}

print("Nested dictionary structure:")
print(students)
print()

print("\n2. ACCESSING NESTED VALUES")
print("Student names:", list(students.keys()))
print()

print("Samantha's grade:", students["Samantha"]["grade"])
print("Alice's GPA:", students["Alice"]["gpa"])
print("Bob's age:", students["Bob"]["age"])
print()

print("Safe access with get():")
grade = students.get("Samantha", {}).get("grade", "Not found")
print(f"Samantha's grade: {grade}")
print()

print("\n3. MODIFYING NESTED VALUES")
print("Before modification:", students["Samantha"])
students["Samantha"]["gpa"] = 3.9
students["Alice"]["grade"] = "Junior"
print("After modification:", students["Samantha"])
print()

students["Bob"]["email"] = "bob@example.com"
print("After adding email:", students["Bob"])
print()

print("\n4. ADDING NEW NESTED DICTIONARIES")
print("Before adding new student:", len(students), "students")
students["Charlie"] = {
    "age": 20,
    "grade": "Junior",
    "gpa": 3.7
}

print("After adding Charlie:", len(students), "students")
print("Charlie's info:", students["Charlie"])
print()

print("\n5. LOOPING THROUGH NESTED DICTIONARIES")
print("All students and their information:")
for student_name, info in students.items():
    print(f"\n{student_name}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
print()

print("Quick summary:")
for name, info in students.items():
    print(f"  {name} - Grade: {info['grade']}, GPA: {info['gpa']}")
print()

print("\n6. DICTIONARIES WITH LISTS")
student_schedule = {
    "Samantha": ["Math", "Science", "History", "English"],
    "Alice": ["Biology", "Chemistry", "Physics"],
    "Bob": ["Calculus", "Linear Algebra", "Statistics"]
}

print("Student schedules:")
print(student_schedule)
print()

print("Samantha's classes:", student_schedule["Samantha"])
print("Number of classes:", len(student_schedule["Samantha"]))
print()

print("Samantha's schedule:")
for i, subject in enumerate(student_schedule["Samantha"], 1):
    print(f"  {i}. {subject}")
print()

print("\n7. COMPLEX NESTED STRUCTURE")
student_profiles = {
    "Samantha": {
        "personal": {
            "age": 20,
            "city": "Honolulu"
        },
        "academic": {
            "grade": "Junior",
            "gpa": 3.8,
            "major": "Computer Science"
        },
        "courses": ["Math", "Science", "History"]
    },
    "Alice": {
        "personal": {
            "age": 19,
            "city": "Boston"
        },
        "academic": {
            "grade": "Sophomore",
            "gpa": 3.9,
            "major": "Biology"
        },
        "courses": ["Biology", "Chemistry"]
    }
}

print("Complex nested structure:")
print(student_profiles["Samantha"])
print()

print("Samantha's city:", student_profiles["Samantha"]["personal"]["city"])
print("Samantha's major:", student_profiles["Samantha"]["academic"]["major"])
print("Samantha's first course:", student_profiles["Samantha"]["courses"][0])
print()

print("\n8. UPDATING COMPLEX NESTED STRUCTURES")

student_profiles["Samantha"]["academic"]["scholarship"] = "Merit"
print("After adding scholarship:", student_profiles["Samantha"]["academic"])
print()

student_profiles["Samantha"]["courses"].append("Computer Science")
print("After adding course:", student_profiles["Samantha"]["courses"])
print()

student_profiles["Alice"]["personal"]["age"] = 20
print("After birthday update:", student_profiles["Alice"]["personal"])
print()

print("\n9. LOOPING THROUGH COMPLEX STRUCTURES")
print("Student profiles:")
for student_name, profile in student_profiles.items():
    print(f"\n{student_name}:")
    print("  Personal Info:")
    for key, value in profile["personal"].items():
        print(f"    {key}: {value}")
    print("  Academic Info:")
    for key, value in profile["academic"].items():
        print(f"    {key}: {value}")
    print("  Courses:")
    for course in profile["courses"]:
        print(f"    - {course}")
print()
