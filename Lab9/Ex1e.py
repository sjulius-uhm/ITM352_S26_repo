# Open the file names.txt and read its contents and print the number of names

file_object = open("names.txt")
contents_list = file_object.readlines()
for name in contents_list: # changes bc it added /n to the end of each name
    print(name.strip())
print(f"Number of names: {len(contents_list)}") 
file_object.close()