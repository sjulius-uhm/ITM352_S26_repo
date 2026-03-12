#add my name and print the entire contents of the file

file_object = open("names.txt")
contents = file_object.read()
file_object.close()

if "Julius, Samantha" not in contents:
    file_object = open("names.txt", "a")
    file_object.write("\nJulius, Samantha")
    file_object.close()

file_object = open("names.txt")
print(file_object.read())
file_object.close()