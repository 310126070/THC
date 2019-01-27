#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que determina si dos listas son iguales
'''

def compara_listas(elemento):
    lista_1 = []
    while elemento != exit:
        lista_1.append(elemento)
        elemento = input('Introducir elemento a lista 1: ')
    
    elemento = input('Introducir elemento a lista 2: ')
    lista_2 = []
    while elemento != exit:
        lista_2.append(elemento)
        elemento = input('Introducir elemento a lista 2: ')
        
    print 'Las listas:', lista_1, 'y', lista_2
    
    if lista_1 == lista_2:
        return "son iguales"
    else:
        return "no son iguales"

    

