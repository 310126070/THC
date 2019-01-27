#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime el promedio de 10 números
'''

from Problema6 import promedio

lista = []
for i in range(10):
    numero = input('Introducir número: ')
    lista.append(numero)
  
print '''El promedio de los números en:
%s
es %g''' % (lista,promedio(lista))

