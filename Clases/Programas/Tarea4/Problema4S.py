#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime el n-ésimo número de Fibonacci
'''

from Problema4 import fibonacci

n=input("Introducir un número: ")

print "El %d° número de Fibonacci es %d" % (n,fibonacci(n))
