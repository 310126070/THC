#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime la suma de los primeros n enteros
'''



def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n-1)


def SUMA(n):
    S = 0
    i = 1
    while i <= n:
        S += i
        i += 1
    return S



        



