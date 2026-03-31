age = input("Enter your age: ")
# opening a file
file = open("file.txt", "r")

# # reading the file
# # method 1 - Read whole file
# f= open("file.txt", "r")
# print(f.read())
# f.close()   

# # method 2 - Read one line
# f= open("file.txt", "r")
# print(f.readline())
# f.close()

# # method 3 - Reads all line as list
# f= open("file.txt", "r")
# print(f.readlines())
# f.close()

# # Writing a file
# # Write to a file (overwrites existing content)
# f = open("file.txt", "w")
# f.write("This is a new line.\n")
# f.write("This will overwrite the existing content.\n")
# f.close()

# # Append to a file (adds to existing content)
# f = open ("file.txt", "a")
# f.write("\n This is Appended Text.")
# f.close()

# # with statement (automatically closes the file)
# with open("file.txt", "r") as f:
#     print(f.read())