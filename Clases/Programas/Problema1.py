def mcd(m,n):
    menor = min(m,n)
    mayor = max(m,n)
    resto = mayor % menor
    if resto == 0:
        return menor
    else:
        return mcd(menor, resto)



def MCD(a,b):
    if a<b:
        tmp=b
        b=a
        a=tmp
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b




print mcd(45,60)
print MCD(60,45)
# 15
print mcd(100,140)
print MCD(100,140)
# 20
