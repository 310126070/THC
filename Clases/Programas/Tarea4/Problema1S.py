#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime el MCD de dos números
'''


from Problema1 import mcd
a=input("Introducir primer número: ")
b=input("Introducir segundo número: ")

print "El MCD de %d y %d es %d" % (a,b,mcd(a,b))
