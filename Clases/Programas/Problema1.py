def mcd(m,n):
    menor = min(m,n)
    mayor = max(m,n)
    resto = mayor % menor
    if resto == 0:
        return menor
    else:
        return mcd(menor, resto)

print mcd(45,60)
# 15
print mcd(100,140)
# 20
