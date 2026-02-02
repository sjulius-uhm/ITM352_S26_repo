# Samantha Julius
# Date: Feb. 1, 2026

first = input("Enter the first name: ")
middleIn = input("Enter the middle initial: ")
last = input("Enter the last name: ")

full_name = first + " " + middleIn + ". " + last
print("Your full name is:", full_name)

print(f"Your full name is: {first} {middleIn}. {last}")

print("Your full name is: %s %s. %s" % (first, middleIn, last))

print("Your full name is: {} {}. {}".format(first, middleIn, last))

print("Your full name is: " + " ".join([first, middleIn + ".", last]))

print("Your full name is: {} {}. {}".format(*[first, middleIn, last]))