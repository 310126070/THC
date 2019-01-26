#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que define la función del área
de un triángulo dados su lados
'''


from math import sqrt

def area_triangulo(a,b,c):
    s = (a+b+c) / 2.0
    return sqrt(s * (s-a) * (s-b) * (s-c))
        



