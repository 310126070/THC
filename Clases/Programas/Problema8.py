def factorial(n):
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n * factorial (n-1)
    return fact




print factorial(0)
print factorial(1)
print factorial(2)
print factorial(3)
print factorial(4)
print factorial(5)
