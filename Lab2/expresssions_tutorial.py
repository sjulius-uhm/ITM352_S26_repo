# Python Arithmetic Expressions Tutorial

# Addition (+): Adds two numbers
print("Addition: 5 + 3 =", 5 + 3)  # Output: 8

# Subtraction (-): Subtracts the second number from the first
print("Subtraction: 10 - 4 =", 10 - 4)  # Output: 6

# Multiplication (*): Multiplies two numbers
print("Multiplication: 6 * 7 =", 6 * 7)  # Output: 42

# Division (/): Divides the first number by the second, returns a float
print("Division: 15 / 4 =", 15 / 4)  # Output: 3.75

# Floor Division (//): Divides and returns the largest integer less than or equal to the result
print("Floor Division: 15 // 4 =", 15 // 4)  # Output: 3

# Modulo (%): Returns the remainder of division
print("Modulo: 15 % 4 =", 15 % 4)  # Output: 3

# Exponentiation (**): Raises the first number to the power of the second
print("Exponentiation: 2 ** 3 =", 2 ** 3)  # Output: 8

# Operator Precedence Examples
# Python follows PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
# Operations with the same precedence are evaluated left to right

print("\nOperator Precedence Examples:")

# Without parentheses: multiplication before addition
print("2 + 3 * 4 =", 2 + 3 * 4)  # Output: 14 (3*4=12, then 2+12)

# With parentheses: parentheses first
print("(2 + 3) * 4 =", (2 + 3) * 4)  # Output: 20

# Exponents before multiplication
print("2 * 3 ** 2 =", 2 * 3 ** 2)  # Output: 18 (3**2=9, then 2*9)

# Mixed operations
print("10 - 2 * 3 + 4 =", 10 - 2 * 3 + 4)  # Output: 8 (2*3=6, 10-6=4, 4+4=8)

# Division and modulo have same precedence, left to right
print("17 // 3 % 2 =", 17 // 3 % 2)  # Output: 1 (17//3=5, 5%2=1)

# String Expressions
# Strings are sequences of characters. You can manipulate them with operators and formatting.

print("\nString Expressions:")

# Concatenation (+): Joins two or more strings
print("Concatenation: 'Hello' + ' World' =", "Hello" + " World")  # Output: Hello World

# Repetition (*): Repeats a string a number of times
print("Repetition: 'Hi' * 3 =", "Hi" * 3)  # Output: HiHiHi

# String Formatting with f-strings: Embed expressions inside strings using f"" and {}
name = "Alice"
age = 25
print(f"Formatting: f'My name is {name} and I am {age} years old.' =", f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.

# More f-string examples
x = 10
y = 20
print(f"Arithmetic in f-string: x + y = {x + y}")  # Output: 20
print(f"Expression: 2 ** 3 = {2 ** 3}")  # Output: 8

# Boolean Expressions
# Boolean expressions evaluate to True or False. Used in conditions and logic.

print("\nBoolean Expressions:")

# Comparison Operators: Compare values
print("Comparison: 5 == 5 =", 5 == 5)  # Equal to: True
print("Comparison: 5 != 3 =", 5 != 3)  # Not equal to: True
print("Comparison: 5 < 10 =", 5 < 10)  # Less than: True
print("Comparison: 5 > 10 =", 5 > 10)  # Greater than: False
print("Comparison: 5 <= 5 =", 5 <= 5)  # Less than or equal to: True
print("Comparison: 5 >= 10 =", 5 >= 10)  # Greater than or equal to: False

# Logical Operators: Combine boolean values
a = True
b = False
print(f"\nLogical: a and b = {a and b}")  # AND: True only if both are True → False
print(f"Logical: a or b = {a or b}")    # OR: True if at least one is True → True
print(f"Logical: not a = {not a}")     # NOT: Inverts the value → False

# Practical Examples
age = 25
has_license = True
print(f"\nPractical: Can drive? age >= 16 and has_license = {age >= 16 and has_license}")  # True
print(f"Practical: Is adult or has license? age >= 18 or has_license = {age >= 18 or has_license}")  # True
print(f"Practical: Not an adult? not (age >= 18) = {not (age >= 18)}")  # False

#Practice Task: Exploring Arithmetic Expressions, I accidently started doing variables
#Calculate your peronal statistics using arithmetic expressions

print("\nExploring Arithmetic Expressions:")

# Calculate your age in days
age = 24  # Replace 24 with your actual age in years
age_in_days = age * 365  # Expression: age × 365
print("Your age in days:", age_in_days) 

# Calculate monthly expenses if you spend $X per week
weekly_spending = 200  # Replace 200 with your actual weekly spending
monthly_expenses = (weekly_spending * 52) / 12  # Expression: Weekly Spending x 52 / 12
print("Your monthly expenses:", monthly_expenses)

# Calculate How many hours you’ve been alive
hours_alive = age_in_days * 24  # Expression: Age in days x 24
print("Hours you've been alive:", hours_alive)

# Calculate Your GPA on a 100-point scale if it’s currently on a 4.0 scale
gpa_4_scale = 3.5  # Replace 3.5 with your actual GPA on a 4.0 scale
gpa_100_scale = (gpa_4_scale / 4.0) * 100  # Expression: (GPA / 4.0) × 100
print("Your GPA on a 100-point scale:", gpa_100_scale)

# Create at least 5 more expressions using your birth year, graduation year, or other personal numbers
# Calculate How many years until you graduate college
current_year = 2026  # Replace 2026 with your current year
graduation_year = 2027  # Replace 2027 with your expected graduation year
years_until_graduation = graduation_year - current_year  # Expression: Graduation Year - Current Year
print("Years until you graduate college:", years_until_graduation)

# Calculate Your Age when you graduate college
age_at_graduation = age + years_until_graduation  # Expression: Current Age
print("Your age when you graduate college:", age_at_graduation)

# Calculate How many hours you've been alive when you graduate college
hours_alive_at_graduation = age_at_graduation * 365 * 24  # Expression: Age at Graduation × 365 × 24
print("Hours you've been alive when you graduate college:", hours_alive_at_graduation)

# Calculate How many hours a month you spend on homework for all your classes if uoi spend X hours a week per class
hours_per_week_per_class = 5  # Replace 5 with your actual hours spent per week per class
number_of_classes = 4  # Replace 4 with your actual number of classes
hours_per_month_homework = (hours_per_week_per_class * number_of_classes * 52) / 12  # Expression: (Hours per week per class × Number of classes × 52) / 12
print("Hours a month spent on homework for all classes:", hours_per_month_homework)

# Calculate How much money you can spend monthly on wants after paying expenses and savings using weekly pay
weekly_pay = 1000  # Replace 1000 with your actual weekly pay
monthly_expenses = 2000  # Replace 2000 with your actual monthly expenses
monthly_income = (weekly_pay * 52) / 12  # Expression: (Weekly
savings = monthly_income * 0.20  # Expression: Monthly Income × 0.20
money_for_wants = monthly_income - (monthly_expenses + savings)  # Expression: Monthly Income - (Monthly Expenses + Savings)
print("Money available for wants after expenses and savings:", money_for_wants)

# Practice Task: Working with Variables in Expressions, I accidently started using string expressions
# Create a personal profile using variables and expressions

print("\nWorking with Variables in Expressions:")

# Store your name, age, hometown, and major in separate variables
name = "Samantha"  # Replace with your actual name
age = 24  # Replace with your actual age
hometown = "Kapolei"  # Replace with your actual hometown
major = "MIS"  # Replace with your actual major

# Print a formatted string introducing yourself using the variables
print(f"Hello, My name is {name} and I'm {age} years old.")
print(f"I'm from {hometown} and I'm majoring in {major}.")

# Calculate age when you started college
starting_college_year = 2023  # Replace with the year you started college
birth_year = 2001  # Replace with your actual birth year
age_when_started_college = starting_college_year - birth_year  # Expression: Starting College Year - Birth Year
print(f"I was {age_when_started_college} years old when I started college.")

# Calculate years until graduation, I did this earlier by accident
print(f"I will graduate college in {years_until_graduation} years.")  

# Use Use your student ID number in mathematical expressions
student_id = 12345678  # Replace with your actual student ID number
last_four_digits = student_id % 10000  # Expression: Student ID % 10000
print(f"The last four digits of my student ID are: {last_four_digits}")

# Create at least 3 complex expressions using your personal data
# Calculate the total hours studied in a semester
weeks_in_semester = 16  # Typical number of weeks in a semester
hours_per_week = 15  # Average hours studied per week
total_hours_studied = weeks_in_semester * hours_per_week  # Expression: Weeks in Semester × Hours per Week
print(f"I studied a total of {total_hours_studied} hours in a semester.")

# Calculate the percentage of your life spent in college
years_in_college = current_year - starting_college_year  # Expression: Current Year - Starting College Year
percentage_life_in_college = (years_in_college / age) * 100  # Expression: (Years in College / Age) × 100
print(f"I have spent {percentage_life_in_college:.2f}% of my life in college.")

# Calculate the estimated age in hours when I graduate college
estimated_age_in_hours_at_graduation = age_at_graduation * 365 * 24  # Expression: Age at Graduation × 365 × 24
print(f"I will be approximately {estimated_age_in_hours_at_graduation} hours old when I graduate college.")

# Practice Task: String Expressions and Operations
# Build your digital identity with string expressions

print("\nString Expressions and Operations:")

# Create a professional email signature using your name, major, and graduation year
graduation_year = 2027  # Replace with your actual graduation year
email_signature = f"Best regards,\n{name}\n{major} Major\nClass of {graduation_year}"
print("\nEmail Signature:\n", email_signature)

# Format your address in different styles (single line, multi-line, formal)
street = "123 Main St"  # Replace with your actual street address
city = "Kapolei"  # Replace with your actual city
state = "HI"  # Replace with your actual state
zip_code = "96707"  # Replace with your actual zip code
single_line_address = f"{street}, {city}, {state} {zip_code}"
multi_line_address = f"{street}\n{city}, {state} {zip_code}"
formal_address = f"{name}\n{street}\n{city}, {state} {zip_code}"
print("\nSingle Line Address:\n", single_line_address)
print("\nMulti-Line Address:\n", multi_line_address)
print("\nFormal Address:\n", formal_address)

# Build social media usernames by combining your initials, birth year, or favorite number
initials = "SJ" # Replace with your actual initials
birth_year = 2001  # Replace with your actual birth year
favorite_number = 7  # Replace with your actual favorite number
username_1 = f"{initials}{favorite_number}"
username_2 = f"{initials}_{birth_year}"
username_3 = f"{initials}{favorite_number}_{birth_year}"
print("\nSocial Media Usernames:")
print("Username 1:", username_1)
print("Username 2:", username_2)
print("Username 3:", username_3)

# Create personalized messages like birthday wishes using your friends’ names
friend_name = "Emily"  # Replace with your friend's actual name
birthday_message = f"Happy Birthday, {friend_name}! Wishing you a fantastic year ahead filled with joy and success!"
print("\nBirthday Message:\n", birthday_message)

# Use f-strings to create a “About Me” paragraph with your hobbies, hometown, and goals
hobbies = "reading, hiking, and coding"  # Replace with your actual hobbies
goals = "to become a successful software engineer"  # Replace with your actual goals
about_me = f"My name is {name}, and I'm from {hometown}. I enjoy {hobbies} in my free time. My goal is {goals}."
print("\nAbout Me:\n", about_me)

# Practice Task: Boolean Expressions and Comparisons
# Create personal decision-making boolean expressions

print("\nBoolean Expressions:")

# Compare your current age to legal milestones (18 for voting, 21 for drinking, 25 for car rental)
can_vote = age >= 18  # Expression: Age >= 18
can_drink = age >= 21  # Expression: Age >= 21
can_rent_car = age >= 25  # Expression: Age >= 25
print(f"Can I vote?", {can_vote})
print(f"Can I drink alcohol? {can_drink}")
print(f"Can I rent a car? {can_rent_car}")

# Check if your GPA meets scholarship requirements or graduation criteria
gpa = 3.5  # Replace with your actual GPA
meets_scholarship = gpa >= 3.0  # Expression: GPA >= 3.0
meets_graduation = gpa >= 2.0  # Expression: GPA >= 2.0
print(f"Do I meet scholarship requirements? {meets_scholarship}")
print(f"Do I meet graduation criteria? {meets_graduation}")

# Create expressions for course prerequisites (e.g., “completed Math 140 AND GPA > 2.0”)
completed_math_140 = True  # Replace with actual completion status
eligible_for_advanced_course = completed_math_140 and (gpa > 2.0)  # Expression: Completed Math 140 AND GPA > 2.0
print(f"Am I eligible for the advanced course? {eligible_for_advanced_course}")

# Build eligibility checks for internships using your class standing and major
class_standing = "Junior"  # Replace with your actual class standing
is_eligible_for_internship = (class_standing in ["Junior", "Senior"]) and (major == "MIS")  # Expression: Class standing is Junior or Senior AND Major is MIS
print(f"Am I eligible for the internship? {is_eligible_for_internship}")

# Write boolean expressions that represent real decisions you make (budget constraints, time management, etc.)
# Budget constraint: Can I afford a new laptop if my budget is $1000 and the laptop costs $850?
budget = 1000  # Replace with your actual budget
laptop_cost = 850  # Replace with the actual laptop cost
can_afford_laptop = budget >= laptop_cost  # Expression: Budget >= Laptop Cost
print(f"Can I afford the new laptop? {can_afford_laptop}")

# Time management: Do I have enough hours in a week to study if I work 20 hours and sleep 56 hours?
total_hours_in_week = 168  # Total hours in a week
work_hours = 20  # Replace with your actual work hours
sleep_hours = 56  # Replace with your actual sleep hours
available_study_hours = total_hours_in_week - (work_hours + sleep_hours)  # Expression: Total Hours - (Work Hours + Sleep Hours)
enough_time_to_study = available_study_hours >= 15  # Expression: Available Study Hours >= 15
print(f"Do I have enough time to study? {enough_time_to_study}")

# Practice Task: Advanced Expression Concepts
#  Apply operator precedence to real financial and academic scenarios

print("\nAdvanced Expression Concepts:")

#Calculate your total semester costs: (tuition + fees) × credit_hours + (housing + meals)
tuition_per_credit = 300  # Replace with your actual tuition per credit hour
fees = 500  # Replace with your actual fees
credit_hours = 15  # Replace with your actual credit hours
housing = 4000  # Replace with your actual housing cost
meals = 2000  # Replace with your actual meal plan cost
total_semester_cost = (tuition_per_credit * credit_hours + fees) + (housing + meals)  # Expression: (Tuition + Fees) × Credit Hours + (Housing + Meals)
print("Total semester costs:", total_semester_cost)

# Determine your final course grade: (homework_avg × 0.3) + (exam_avg × 0.7)
homework_avg = 85  # Replace with your actual homework average
exam_avg = 90  # Replace with your actual exam average
final_course_grade = (homework_avg * 0.3) + (exam_avg * 0.7)  # Expression: (Homework Avg × 0.3) + (Exam Avg × 0.7)
print("Final course grade:", final_course_grade)

# Plan your monthly budget: income - (rent + utilities + groceries + entertainment)
monthly_income = 3000  # Replace with your actual monthly income
rent = 1000  # Replace with your actual rent
utilities = 200  # Replace with your actual utilities cost
groceries = 400  # Replace with your actual groceries cost
entertainment = 150  # Replace with your actual entertainment cost
monthly_budget = monthly_income - (rent + utilities + groceries + entertainment)  # Expression: Income - (Rent + Utilities + Groceries + Entertainment)
print("Monthly budget after expenses:", monthly_budget)

# Compare study time allocation: hours_per_week ÷ number_of_courses vs. recommended_hours
hours_per_week = 20  # Replace with your actual study hours per week
number_of_courses = 4  # Replace with your actual number of courses
recommended_hours = 5  # Replace with your actual recommended hours per course
study_time_per_course = hours_per_week / number_of_courses  # Expression: Hours per Week ÷ Number of Courses
meets_recommendation = study_time_per_course >= recommended_hours  # Expression: Study Time
print("Do I meet the recommended study hours per course?", meets_recommendation)

# Create expressions where parentheses change your GPA calculation
homework_avg = 88  # Updated homework average
exam_avg = 92  # Updated exam average
participation_avg = 95  # New participation average
extra_credit = 3  # Extra credit points
final_gpa_with_parentheses = ((homework_avg * 0.3) + (exam_avg * 0.6) + (participation_avg * 0.1)) / 100 + extra_credit  # Expression with parentheses
final_gpa_without_parentheses = (homework_avg * 0.3) + (exam_avg * 0.6) + (participation_avg * 0.1) / 100 + extra_credit  # Expression without parentheses
print("Final GPA with parentheses:", final_gpa_with_parentheses)
print("Final GPA without parentheses:", final_gpa_without_parentheses)

# Create expressions where parentheses change your graduation timeline
credits_needed = 120  # Total credits needed to graduate
credits_completed = 90  # Credits already completed
credits_per_semester = 15  # Credits taken per semester
semesters_per_year = 2  # Semesters per year
years_until_graduation_with_parentheses = (credits_needed - credits_completed) / (credits_per_semester * semesters_per_year)  # Expression with parentheses
years_until_graduation_without_parentheses = credits_needed - credits_completed / credits_per_semester
print("Years until graduation with parentheses:", years_until_graduation_with_parentheses)
print("Years until graduation without parentheses:", years_until_graduation_without_parentheses)

# End of Python Arithmetic Expressions Tutorial