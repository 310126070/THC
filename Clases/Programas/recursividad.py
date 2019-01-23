#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def fib(n):
    """Calcula el n-ésimo término
de la sucesión de Fibonacci
"""
    if n>2:
        return fib(n-1) + fib(n-2)
    else:
        return 1


def suma(n):
    if n==1:
        return 1
    else:
        return n + suma(n-1)



def printr(L):
    if L:
        print L[0],
        printr(L[1:])
    else:
        None

def printr1(L):
    if len(L)>1:
        print L[0],
        printr(L[1:])
    else:
        print(L[0])
        
printr([8,7,4,5,3,2,1,])
printr1([8,7,4,5,3,2,1,])

# http://www.pythontutor.com/visualize.html
