#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime si un entero
suministrado como argumento es primo
'''


from Problema3 import primo

n = input("Introducir un número: ")

print "El número %d %s" % (n,primo(n))
