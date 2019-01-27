#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que calcula el promedio de 10 números
'''

def suma(su):   
    i = 2
    s = 0.0
    while i <= 10:
        s = s + su
        su = input("Introducir el %d° número: " % (i))
        i = i + 1
    return s / 10
        
    


