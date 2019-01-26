#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que define la función de la distancia
entre dos puntos en el plano dadas sus coodenadas
'''


from math import sqrt

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    suma_cuadrados = dx**2 + dy **2
    return sqrt(suma_cuadrados)

        



