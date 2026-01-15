# loops
# for loops
for i in range(1, 6):
    print(i)

for i in range(5):        # 0 to 4
    print(i)

for i in range(2, 11, 2):  # even numbers
    print(i)

# Practice Questions
# Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# Print odd numbers from 1 to 50
for i in range(1,51,2):
    print(i)

# Print table of 7
for i in range (1, 11):
    print("7 x", i, "=", 7*i)
    
# looping through a string
name = "Python"

for ch in name:
    print(ch)

# Practice Questions
# Count vowels in a string
string= input("enter a string: ")
vowels = "aeiouAEIOU"
count=0
for ch in string:
    if ch in vowels:
        count +=1
    print("Number of vowels: ", count)
    
# Print each character on new line
string = input("enter a string: ")
for ch in string:
    print (ch)
    
# looping thorugh a list
marks = [80, 75, 90]

for m in marks:
    print(m)

# Practice Questions
# Find sum of list elements
list = int(input("enter number of elements in list: "))
total = 0
for i in range (list):
    num = int(input("enter element: "))
    total +=num
print("sum of elements: ", total)

# Find maximum element
list = int(input("enter number of elements in list:"))
max_num = float('-inf')
for i in range (list):
    num = int(input("enter element: "))
    if num > max_num:
        max_num = num
print("maximum element is: ", max_num)

# while loops
i = 1
while i <= 5:
    print(i)
    i += 1

# Practice Questions
# Print numbers from 10 to 1
i =10
while i >= 1:
    print(i)
    i -=1

# Print factorial of a number
n= int(input("enter a number: "))
factorial = 1
i = 1
while i<= n:
    factorial *=i
    i +=1
    print("factorial is : ", factorial)
    
# loop control statements
# break statement
for i in range(1, 10):
    if i == 6:
        break
    print(i)

# Practice Questions
# Stop loop when number becomes 8
for i in range(1, 20):
    if i == 8:
        break
    print(i)

# Exit loop if user enters 0
while True:
    num = int(input("enter a number (0to exit): "))
    if num ==0:
        break
    print("you entered: ", num)
    
# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Practice Questions
# Skip number 5
for i in range(1, 10):
    if  i ==5:
        continue
    print(i)

# Skip even numbers
for i in range (1, 21):
    if i %2 ==0:
        continue
    print(i)
    
# pass statement
for i in range(5):
    pass

# nested loops 
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        
# Practice Questions
# Print number pattern
for i in range(1, 10):
    for j in range(1, i+1):
        print(j , end=' ')
    print()

# Print star pattern
for i in range(1, 12):
    for j in range (1, i+1):
        print("*",end=' ')
    print()
      
# common loop programs
# Sum of Natural Numbers
sum = 0
for i in range(1, 11):
    sum += i

print(sum)

# Factorial of a Number
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

# Prime Number Check
n = 7
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False
        break

if flag:
    print("Prime")
else:
    print("Not Prime")