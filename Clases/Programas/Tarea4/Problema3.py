#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070

Taller de herramientas computacionales


Programa que define las equivalencias
entre grados centígrados y Fahrenheit
'''


def conversion(a,G):
    if a == 1:
        return 5 * ( G - 32 )  / 9 
    if a == 2:
        return ( 9 * G ) / 5 + 32

