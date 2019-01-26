#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que define la función factorial 
'''


def factorial(n):
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n * factorial (n-1)
    return fact
