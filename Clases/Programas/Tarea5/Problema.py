lista = []
numero = input('Introduce: ')
while numero == exit:
    lista.append(numero)
    numero = input('Introduce: ')

print lista



n = input('cuantos elementos: ')
lista1 = []
for i in range(n):
    elemento = input('Introduce:')
    lista1.append(elemento)

print lista1


    
m = input('cuantos elementos: ')
lista2 = []
for i in range(m):
    elemento = input('Introduce:')
    lista2.append(elemento)



print lista2

if n == m:
    print "son iguales"
else:
    print "no son iguales"
