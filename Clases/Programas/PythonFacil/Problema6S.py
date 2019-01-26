#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime la resolución del juego de las Torres de Hanoi
'''


from Problema6 import hanoi

n=input("Introducir el número de discos: ")
inicial=input("Indicar la aguja inicial: ")
final=input("Indicar la aguja final: ")
libre=input("Indicar la aguja libre: ")

print hanoi(n,inicial,final,libre)
