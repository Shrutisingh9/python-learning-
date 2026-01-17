# functions
def greet():
    print("Hello, Welcome to Python!")

# calling theh function 
greet()

# function without parameters and without returns
def show_message():
    print("Python is powerful")

show_message()

# function with parameters
def greet(name):
    print("Hello", name)
    
greet("shruti")

# function with multiple parameters
def add(a, b):
    print("sum =", a+b)
    
add(10, 20)

# function wiht return statement
def square(n):
    return n*n

result = square(5)
print(result)

# function without return (implicit return)
def demo():
    print("Hello")
    
print(demo())

# default arguments
def greet(name = "User"):
    print("Hello", name)
    
greet()
greet("shruti")

# keyword arguments
def student(name, age):
    print(name, age)
    
student( age = 20, name ="shruti")

# varable length arguments
# *args
def add_numbers(*args):
    print(sum(args))
    
add_numbers(10, 20, 30)

# local variables
def test():
    x = 10
    print(x)
    
# gloabl variables
x = 5

def show():
    print(x)
    
show()

# gobal keyword
x =10 
def change():
    global x
    x = 20 

change()
print(x)

# function calling another function 
def add (a, b):
    return a + b

def multiply(a, b):
    return add(a, b)*2

print(multiply(3, 4))

# examples questions
# even or odd
def check_even_odd(n):
    if n % 2 ==0:
        return "Evev"
    else:
        return "odd"
    
print(check_even_odd(7))

# factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    return fact

print(factorial(5))

# simple calculator
def calculator(a, b):
    print("Add:", a+b)
    print("Sub:", a-b)     
    print("Mul:", a*b)
    print("Div:", a/b)
    
calculator(10, 5)

# practice question
# write a function to print your name
def name():
    print("Shruti Singh")
name()

# write a function to add two numbers
def add(a, b):
    return a +b

print(add(15, 21))

# write a function to find square of a number
def square(n):
    return n*n
print(square(7))

# write a function to check if a number is prime
def prime(n):
    if n <=1:
        return "not prime"
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            return "not prime"
    return "prime"

print(prime(11))

# write a function to reverse a number
def reverse(n):
    rev =0
    while n>0:
        digit = n %10
        rev = rev * 10 + digit
        n = n //10
    return rev
print(reverse(1234))

# Write a function to find maximum of 3 numbers.
def maximum (a, b, c):
    return max(a, b , c)

print(maximum(10, 234, 56))

# Write a function to count vowels in a string.
def vowel(s):
    count=0
    for char in s.lower():
        if char in 'aeiou':
            count += 1
    return count
print(vowel("Hello World!"))

# Write a function to check palindrome number.
def palindrome(n):
    temp = n 
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev *10 + digit
        n = n //10
        
    if temp == rev:
        return "palindrome"
    else:
        return "not palindrome"

print(palindrome(1232))
        
# Write a function to calculate LCM of two numbers.
def LCM(a, b):
    x, y = a, b
    
    while y != 0:
        x, y = y , x%y
    gcd = x
    lcm = (a*b)//gcd
    return lcm

a = int(input("enter first number to calculate LCM: "))
b = int(input("enter second number to calculate LCM: "))
print(LCM(a, b))

# Write a function to return list of even numbers from given list.
def even (lst):
    even_num = []
    for num in lst:
        if num % 2 == 0:
            even_num.append(num)
    return even_num
lst = int(input("enter number of elements in list: "))
numbers=[]
for i in range(lst):
    n = int(input("enter elements:"))
    numbers.append(n)
print(even(numbers))

# Write a function to generate Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    count = 0
    
    while count< n :
        print(a, end=" ")
        a, b = b, a+b
        count +=1
    return fibonacci

n = int(input("enter numbers of terms in fibonacci series: "))
print(fibonacci(n))

# Write a function that takes a list and returns:
def list(numbers):
# sum
    total = sum (numbers )
# average
    avg = sum (numbers)/ len(numbers)
# maximum
    maximum = max(numbers)
# minimum
    minimum = min(numbers)

    return total , avg, maximum, minimum
n = int(input("enter number of elements in list: "))
numbers=[]
for i in range(n    ):
    num = int(input("enter elements:"))
    numbers.append(num)       
total, avg, maximum, minimum = list(numbers)
print("sum : ", total)
print("average : ", avg)
print("maximum : ", maximum)
print("minimum : ", minimum)    

