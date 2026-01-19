def square(n):
    return n * n

def cube(n):
    return n * n * n

def power(base, exp):
    return base ** exp

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result