# Create a dictionary for student information (name, age, grade, subjects).
# Samantha Julius
# Feb. 2, 2026

# Create the student information dictionary
student_info = { 
    "name": "Samantha Julius", 
    "age": 20, 
    "grade": "Junior", 
    "subjects": ["Math", "Science", "History"] 
}

# Display the complete dictionary
print("Student Information:", student_info)
print()

# Access individual values
print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Grade:", student_info["grade"])
print("Subjects:", student_info["subjects"])
print()

# Add new information
student_info["gpa"] = 3.8
student_info["email"] = "sjulius@example.com"
print("After adding GPA and email:", student_info)
print()

# Update existing information
student_info["age"] = 21  # Birthday!
print("After birthday (age updated):", student_info)
print()

# Add a new subject
student_info["subjects"].append("Computer Science")
print("After adding new subject:", student_info["subjects"])
print()

# Display all keys and values
print("All keys:", list(student_info.keys()))
print("All values:", list(student_info.values()))
print()

# Check if a key exists
if "gpa" in student_info:
    print(f"GPA: {student_info['gpa']}")
    
# Count number of subjects
print(f"Total subjects enrolled: {len(student_info['subjects'])}")