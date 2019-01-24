#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que calcula el promedio 
'''

def suma(a):   
    i = 1
    s = 0.0
    while i <= a:
        su = input("Introducir el %d° número: " % (i))
        s = s + su
        i = i + 1
    return s / a
        
    


