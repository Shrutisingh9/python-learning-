# try except block
try:
    a = int(input("Enter a number: "))
    print(10/a)
except :
    print("Error occurred")
    
    
# handling specific exceptions
try:
    x = int(input("Enter a number: "))
    print(10/x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input. Please enter a number.")