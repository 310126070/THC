#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa define la función del promedio de 10 números
'''

def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma/10.0


