#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime si dos funciones son iguales
'''

from Problema1 import compara_listas

print '''Utilizar "exit" para terminar de
añadir elementos a las listas''' 

elemento = input('Introducir elemento a lista 1: ')

print '%s' % (compara_listas(elemento))


