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
    for i in range(2, int(n**0,5)+1):
        if n % i ==0:
            return "not prime"
    return "prime"

print(prime(11))

# write a function to reverse a number
