# Open the file names.txt and read its contents and print the number of names
count = 0

with open("names.txt") as file_object:
    while (line := file_object.readline()):
        print(line.strip())
        count += 1

print(f"Number of names: {count}")