#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070

Taller de herramientas computacionales

Programa que imprime las equivalencias
entre grados centígrados y Fahrenheit
'''


from Problema3 import conversion
a = input('''Presione 1 para convertir grados Fahrenheit a centígrados
       o 2 para convertir grados centígrados a Fahrenheit: ''')
G = input("Introducir los grados a convertir: " )


print "Equivalen a %g°" % (conversion(a,G))
