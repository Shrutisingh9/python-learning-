# make a simple calculator using python that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.

num1 =(input("Enter first number: "))
num2 =(input("Enter second number: "))

print("choose the operation you want to perform:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = float(num1) + float(num2)
    print(f"The sum of {num1} and {num2} is: {result}")
elif choice == '2':
    result = float(num1) - float(num2)
    print(f"The difference between {num1} and {num2} is: {result}")     
elif choice == '3':
    result = float(num1) * float(num2)
    print(f"The product of {num1} and {num2} is: {result}")
elif choice == '4':  
    if float(num2) != 0:
        result = float(num1) / float(num2)
        print(f"The division of {num1} by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input! Please select a valid operation.")