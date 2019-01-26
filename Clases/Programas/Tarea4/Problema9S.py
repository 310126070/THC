#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime el área de
un triángulo dados sus lados
'''


from Problema9 import area_triangulo

a = input("Introducir el primer lado: ")
b = input("Introducir el segundo lado: ")
c = input("Introducir el tercer lado: ")

print "El área del triángulo de lados %g, %g y %g, es %g" % (a,b,c,area_triangulo(a,b,c))



