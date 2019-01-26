#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa de la función
'''


from math import sin, pi

def H_eps(x,eps=0.01):
    if x < -eps:
        return 0
    elif x >= -eps and x <= eps:
        return 1/2 + x/(2*eps) + 1/(2*eps)*(sin(pi*x/eps))
    else:
         return 1
