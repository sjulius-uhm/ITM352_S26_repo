# Practice each method with your student dictionary.
# Samantha Julius
# Feb. 2, 2026

student_info = {
    "name": "Samantha Julius",
    "age": 20,
    "grade": "Junior",
    "subjects": ["Math", "Science", "History"],
    "gpa": 3.8
}

print("1. keys() METHOD")
keys = student_info.keys()
print("All keys:", list(keys))
print("Type:", type(keys))
print()

print("\n2. values() METHOD")
values = student_info.values()
print("All values:", list(values))
print("Type:", type(values))
print()

print("\n3. items() METHOD")
items = student_info.items()
print("All items:", list(items))
print()
print("Looping through items:")
for key, value in student_info.items():
    print(f"  {key}: {value}")
print()

print("\n4. get() METHOD")
name = student_info.get("name")
print(f"Name: {name}")
email = student_info.get("email")
print(f"Email: {email}")
email = student_info.get("email", "Not Available")
print(f"Email (with default): {email}")
print()

print("\n5. update() METHOD")
print("Before update:", student_info)
student_info.update({"email": "sjulius@example.com", "age": 21})
print("After update:", student_info)
print()

print("\n6. pop() METHOD")
print("Before pop:", student_info)
removed_email = student_info.pop("email")
print(f"Removed email: {removed_email}")
print("After pop:", student_info)
phone = student_info.pop("phone", "No phone number")
print(f"Tried to pop phone: {phone}")
print()

print("\n7. clear() METHOD")
temp_dict = student_info.copy()
print("Before clear:", temp_dict)
temp_dict.clear()
print("After clear:", temp_dict)
print("Is empty?", len(temp_dict) == 0)
print()

print("FINAL STUDENT DICTIONARY (original preserved)")
print(student_info)