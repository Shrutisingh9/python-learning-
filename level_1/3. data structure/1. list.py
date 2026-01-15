# list
# creating a lsit
numbers = [1, 2, 3, 4]

# accessingn elements
print(numbers[0])  # Output: 1
print(numbers[-1]) # Output: 4

# modifying elements
numbers[1] =10
print(numbers)  # Output: [1, 10, 3, 4]

# addingn elements
numbers.append(5)
numbers. insert(1, 20)
print(numbers)  # Output: [1, 20, 10, 3, 4, 5]

# removing elements
numbers.remove(10)
numbers.pop()
print(numbers)  # Output: [1, 20, 3, 4]

# practive questions
# Create list of 5 numbers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

# Find sum of elements
total = 0
for num in list:
    total += num
print("sum of elements: ", total)

# Find maximum element
max_num = max(list)
print("maximum element is: ", max_num)
        
# reverse a list
list.reverse()
print("reversed list: ", list)

# count even numbers
even_count = 0
for num in list:
    if num % 2 == 0:
        even_count += 1
print("count of even numbers: ", even_count)
    