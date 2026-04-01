# opening a file
file = open("level_3/file.txt", "r")

# reading the file
# method 1 - Read whole file
f= open("level_3/file.txt", "r")
print(f.read())
f.close()   

# method 2 - Read one line
f= open("level_3/file.txt", "r")
print(f.readline())
f.close()

# method 3 - Reads all line as list
f= open("level_3/file.txt", "r")
print(f.readlines())
f.close()

# Writing a file
# Write to a file (overwrites existing content)
f = open("level_3/file.txt", "w")
f.write("This is a new line.\n")
f.write("This will overwrite the existing content.\n")
f.close()

# Append to a file (adds to existing content)
f = open ("level_3/file.txt", "a")
f.write("\n This is Appended Text.")
f.close()

# with statement (automatically closes the file)
with open("level_3/file.txt", "r") as f:
    print(f.read())
    
# file methods
with open("level_3/file.txt", "r") as f:
    print(f.tell())  # Get current position
    f.seek(2) # Move to the beginning of the file
    print(f.read())  # Read from the new position
    
# check file existence
import os
if os.path.exists("level_3/file.txt"):
    print("File exists")
else:
    print("File does not exist")

# Deleting a file
os.remove("data.txt")

# renaming a file
os.rename("old_name.txt", "new_name.txt")