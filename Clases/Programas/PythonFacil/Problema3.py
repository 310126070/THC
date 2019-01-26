#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que define una función que determina
si un entero suministrado como argumento es primo
'''


def primo(n):
    si_satisface = True
    divisor = 2
    while divisor < n and si_satisface:
        if n % divisor == 0:
            si_satisface = False
        divisor += 1
    if si_satisface:
        return 'es primo'
    else:
        return 'no es primo'


    
