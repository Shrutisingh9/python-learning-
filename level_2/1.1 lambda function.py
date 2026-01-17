# lambda functions
# syntax: lambda arguments: expression
add = lambda a, b: a+b
print(add(5, 3))

# Example 1: Square of a Number
square = lambda x: x * x
print(square(6))

# Example 2: Even or Odd
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(7))

# Example 3: Maximum of Two Numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))

# lambda with map()
# syntax: map(functiom, iterable)

# Example: Square of List Elements
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * x, numbers))
print(result)

# lambda with filter()
# syntax: filter(function, iterable)    
# Example: Even Numbers
numbers = [10, 15, 20, 25, 30]
even = list(filter(lambda x: x %2 == 0, numbers))
print(even)

# lambda with reduce()
# syntax: from functools import reduce
# reduce(function, iterable)

# Example: sum of list
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)

# lambda with sorting
# Example: Sort List of Tuples
data = [(1, 3), (4, 1), (2, 2)]
data.sort(key=lambda x: x[1])
print(data)

# Lambda Inside Function
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(5))

# practical examples
# Example 1: Add 10 to Each Element
lst = [1, 2, 3]
result = list(map(lambda x: x + 10, lst))
print(result)

# Example 2: Filter Names Starting with 'A'
names = ["Amit", "Rahul", "Anita", "Suman"]
result = list(filter(lambda name: name[0] == 'A', names))
print(result)

# Example 3: Find Maximum Number in List
from functools import reduce

nums = [10, 40, 30]
max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num)

# PRACTICE QUESTIONS
# Write a lambda function to find cube of a number.
cube= lambda x: x**3
print(cube(4))

# Write a lambda to add two numbers.
add = lambda a, b : a+b
print(add(12, 3))

# Use lambda with map() to double all elements in a list.
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# Use lambda with filter() to find odd numbers.
nums = [1, 2, 3,4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, nums))
print(odd_numbers)

# Use lambda to find maximum of 3 numbers.
max = lambda a, b, c: a if (a>b and b>c) else (b if (b>a and b>c) else c)
print(max(10, 25, 14))

# Use lambda with reduce() to find product of list.
from functools import reduce
num = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a*b, num)
print(product)

# Sort list of strings based on length using lambda.
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)