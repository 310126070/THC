#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime la integral de 2x + 5x^2 - 6x^3 + 12
'''


def integral(a,b,n):
    if n == 0:
        suma = 0
    else:
        deltax = (b-a) / float(n)
        suma = 0
        for i in range(n):
            suma += deltax * ( 2*(a + i * deltax) + 5*(a + i * deltax)**2 - 6*(a + i * deltax)**3 + 12 )
    return suma
