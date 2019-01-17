def suma(n):
    if n == 1:
        S = 1
    else:
        S = n + suma(n-1)
    return S


print suma(1)
print suma(2)
print suma(3)
print suma(4)
print suma(5)
print suma(6)
print suma(7)
print suma(8)



