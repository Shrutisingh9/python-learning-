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