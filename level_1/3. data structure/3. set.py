# set
nums = {1, 2, 3, 3}
print(nums)

# Accessing Elements
nums.add(4)
nums.remove(2)
print(nums) 

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) #union
print(a & b) #intersection
print(a - b) #difference
print(a ^ b) #symmetric difference

# Practice Questions
# Remove duplicates from list using set
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print("Unique elements: ", unique_set)

# Find common elements
common_elements = a & b
print("Common elements: ", common_elements)

# Perform union & intersection
union_result = a | b
intersection_result = a & b
print("Union: ", union_result)
print("Intersection: ", intersection_result)    