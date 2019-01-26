#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que resuelve el juego de las Torres de Hanoi
'''


def hanoi(n,inicial,final,libre):
    if n == 1:
        print 'Se mueve el disco superior de aguja %d a %d' % (inicial,final)
    else:
        if inicial != 1 and final !=1:
            libre = 1
        elif inicial != 2 and final !=2:
            libre = 2
        else:
            libre = 3
        hanoi(n-1,inicial,libre,final)
        print 'Se mueve el disco superior de aguja %d a %d' % (inicial,final)
        hanoi(n-1,libre,final,inicial)
