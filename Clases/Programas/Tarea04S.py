#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que calcula la integral de 2x + 5^2 - 6x^3 + 12
'''


from Tarea04 import integral

a = input('Inicio del intervalo: ')
b = input('Final del intervalo: ')
n = input('Número de rectángulos: ')

print 'La integral entre %g y %g es aproximadamente %f' % (a,b,integral(a,b,n))



