# operators
# arithmetic operators
a=10
b=3
print("addition:" , a+b)
print("subtraction" , a-b)
print("multiplication" ,a*b)
print("division", a/b)
print("modulus", a%b)
print("floor division", a//b)
print("exponent", a**b)

# Practice Questions
# Add two numbers
n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
sum=n+m
print("sum", sum)

# Find remainder of 23 ÷ 4
a=23
b=4
reminder=a%b
print("reminder", reminder)

# Find square and cube of a number
num=int(input("enter a number:"))
square=num**2
cube=num**3
print("square", square)
print("cube", cube)

# Relational (Comparison) Operators
a=10
b=5
print("a equal to b:", a==b)
print("a not equal to b:", a!=b)
print("a greater than b:", a>b)
print("a less than b:", a<b)
print("a greater than or equal to b:", a>=b)
print("a less than or equal to b:", a<=b)

# Practice Questions
# Compare two numbers
x=int(input("enter first number: "))
y=int(input("enter second number: "))
if x>y:
    print("x is greater than y")
elif x<y:
    print("x is less than y")
else:
    print("x is equal to y")

# Check if age ≥ 18
age=int(input("enter your age: "))
if age>=18:
    print("age is 18 or older")
else:
    print("age is less than 18")
    
# logical operators
age = 20
marks = 65

print(age >= 18 and marks >= 40)
print(age < 18 or marks >= 40)
print(not age < 18)

# assignment operators
x = 10
x += 5
print(x)
x *= 2
print(x)
x -= 4
print(x)
x /= 3
print(x)
x %= 4
print(x)

# Practice Questions
# Use += operator
num=int(input("Enter a number: "))
num += 10
print("After adding 10:", num)  

# Use *= operator
num=int(input("Enter a number: "))
num *= 5
print("After multiplying by 5:", num)

# membership operators
list1 = [10, 20, 30]

print(20 in list1)
print(50 not in list1)

list1 = [10, 20, 30]

print(20 in list1)
print(50 not in list1)

# Practice Questions
# Check if name exists in list
names = ["Alice", "Bob", "Charlie"]
name_to_check = input("Enter a name to check: ")
if name_to_check in names:
    print(f"{name_to_check} exists in the list.")
else:
    print(f"{name_to_check} does not exist in the list.")

# Check if number not in tuple
numbers= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num_to_check = int(input("enter a number to check: "))
if num_to_check not in numbers:
    print(f"{num_to_check} is not in the tuple.")
else:
    print(f"{num_to_check} is in the tuple.")   
    
# identity operators
a = 10
b = 10

print(a is b)
print(a is not b)

# Practice Questions
# Use is operator
x=[1,2,3,4,5,6]
y=x
if x is y:
    print("x and y refer to the same object.")
else:
    print("x and y refer to different objects.")

# Compare two variables
m=100
n=200
if m is not n:
    print("m and n refer to different objects.")
else:
    print("m and n refer to the same objects.")