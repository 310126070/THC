#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que calcula el promedio de 10 números
'''

def prom_min_max(numero):
    
    i = 2
    suma = 0
    minimo = numero
    maximo = numero
    
    while i <= 10:
        
        suma = suma + numero
        
        numero = input("Introducir el %d° número: " % (i))
        
        if minimo <= numero:
            minimo = minimo
        else:
            minimo = numero

        if maximo >= numero:
            maximo = maximo
        else:
            maximo = numero
               
        i = i + 1
        
    print 'El promedio es',float(suma)/10,'el mínimo',minimo,'y el máximo',maximo
    


        
    


