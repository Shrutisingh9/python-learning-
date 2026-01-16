# dictinoary
student = {
    "name": "Shruti",
    "age": 20,
    "marks": 85
}

# accessing values
print(student["name"])  # Output: Shruti
print(student.get("age"))  # Output: 20 

# updating & adding
student["marks"] = 90  # updating
student["city"] = "Delhi"  # adding new key-value pair
print(student)

# removing
del student["age"]
marks = student.pop("marks")
print(student)

# looping dictinonary
for key, value in student.items():
    print(key, value)
    
# Practice Questions
# Create student dictionary
student = {
    "name": "Shruti",
    "age": 20,
    "marks": 85
}

# Update marks
student["marks"] = 90
print("Updated marks: ", student["marks"])

# Print all keys & values
for key, value in student.items():
    print(key, ":", value)

# Count total elements
total_elements = len(student)
print("Total elements in dictionary: ", total_elements)