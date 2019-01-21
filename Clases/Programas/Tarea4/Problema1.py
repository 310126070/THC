#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que calcula el MCD de dos números
'''


def mcd(a,b):
    if a%b == 0:
        return b
    else:
        return mcd(b,a%b)


def MCD(a,b):
    if a<b:
        tmp=b
        b=a
        a=tmp
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b




