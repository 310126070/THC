#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime la distancia
entre dos puntos en el plano dadas sus coodenadas
'''


from Problema10 import distancia

x1 = input("Introducir la coordena x1: ")
y1 = input("Introducir la coordena y1: ")
x2 = input("Introducir la coordena x2: ")
y2 = input("Introducir la coordena y2: ")

print '''La distancia entre los puntos
P1(%g,%g) y P2(%g,%g) es %g''' % (x1,y1,x2,y2,distancia(x1, y1, x2, y2))



