# modules
# importing modules
# method 1: import whole module
import math
print(math.sqrt(16))

# method 2: import specific function 
from math import sqrt
print(sqrt(25))

# method 3: import with alias
import math as m
print(m.pi)

# method 4: import everything
from math import *
print(sin(0))

# nbuilt in modules
# math module
import math
print(math.sqrt(49))
print(math.factorial(5))
print(math.pow(2, 3))
print(math.pi)

# random Module
import random
print(random.randint(1, 10))
print(random.choice([10, 20, 30]))
print(random.random())

# datetime Module
import datetime
now = datetime.datetime.now()
print(now)
print(now.date())
print(now.time())

# os Module
# import os
# print(os.getcwd())
# os.mkdir("test_folder")

# sys Module
import sys
print(sys.version)
print(sys.path)

# practicalexamples
# Example 1: Random Password Generator
import random
password = random.randint(1000, 9999)
print(password)

# Example 2: Date Difference
from datetime import date
d1 = date(2024, 1, 1)
d2 = date.today()
print(d2 - d1)

# PRACTICE QUESTIONS
# Import math module and find square root of 64.
import math
print(math.sqrt(64))

# Use random module to generate a number between 1 and 50.
import random
print(random.randint(1, 50))

# Create your own module with functions:
# add
def add(a, b):
    return a+b

# multiply
def mul(a, b):
    return a*b

# Import only one function from math module.
from math import sqrt
print(sqrt(81))

# Create a module to check:

# prime number
def prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n %i ==0:
            return False
    return True

n = int(input("enter a number: "))
if prime(n):
    print(n, "is prime number")
else:
    print(n, "is not prime number")

# palindrome number
def palindrome(n):
    return str(n) == str(n)[::-1]
n = int(input("enter a number: "))
if palindrome(n):
    print(n, "is palindrome")
else:
    print(n, "is not palindrome")