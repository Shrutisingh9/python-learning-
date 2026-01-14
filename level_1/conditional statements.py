#conditional_statements.py
# if statement
age = 19

if age >= 18:
    print("Eligible to vote")
# Flow Explanation
# Check age >= 18
# If true → print message
# If false → do nothing

# Practice Questions
# Check if number is positive
num= int(input("enter a number: "))
if num >0:
    print("number is postive")

# Check if student passed (marks ≥ 40)
marks= int(input("enter your marks: "))
if marks >=40:
    print("student has passed")
    
# if-else statement
num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Practice Questions
# Check even or odd
num =int(input("enter a number: "))
if num % 2 ==0:
    print("even number")
else:
    print("odd number")

# Check adult or minor
age = int(input("enter your age: "))
if age >=18:
    print("adult")
else:
    print("minor")
    
# if-elif-else statement
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Practice Questions
# Grade system
marks = int(input("enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:       
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Greatest of three numbers
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>=b and a>=c:
    print("a is greatest")
elif b>=a and b>=c:
    print("b is greatest")
else:
    print("c is greatest")

# nested if statements
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

# Practice Questions
# Check login system
username = input("enter username:")
password = input("enter password:")
if username == "admin" :
    if password == "password1234":
        print("login sucessfully")
    else:
        print("incorrect password")
else:
    print("username not found")

# Check exam eligibility
age = int(input("enter your age: "))
admit_card = input("do you have admit card (yes/no): ")
if age >=18:
    if admit_card == "yes":
        print("eligible for exam")
    else:
        print("admit card required")
else:
    print("not eligible for exam ")

# conditional statement (short-hand if statement)
a = 10
b = 20

print("A is larger") if a > b else print("B is larger")

# Practice Questions
# Check even/odd using short-hand
num = int(input("enter a number: "))
print("even number") if num % 2 ==0 else print("odd number")

# Find greater number
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("a is greater") if a > b else print("b is greater")   