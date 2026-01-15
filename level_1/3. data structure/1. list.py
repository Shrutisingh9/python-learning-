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
list= [1, 2, 3, 4, 5]
print(list)

# Find sum of elements
elements= int(input("enter number of elements in list: "))
total =0
for i in range (elements):
    num = int(input("ener element: "))
    total +=num
print("sum of elements: ", total)

# Find maximum element
max = int(input("enter number of elements in list to find maximum: "))
max = float('-inf')
for i in range (elements):
    num = int(input("enter elements: "))
    if num > max:
        max = num
print("maximum element: ", max)
# Reverse a list
list = int(input("enter number of element on the list to reverse: "))
reversed_list = []
for i in range (list):
    num = int(input("enter elements: "))
    reversed_list.insert(0, num)
    continue
print("reversed list is: ", reversed_list)
    
# Count even numbers
list = int(input("enter number of elements in list to count even numbers: "))
count = 0
for i in range (list):  
    num = int(input("enter elements: "))
    if num % 2 == 0:
        count += 1
print("count of even numbers: ", count)
