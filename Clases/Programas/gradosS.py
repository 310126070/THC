# -*- coding: utf-8 -*-

from grados import *
L1=listaC(-15,32,10)
L2=listaF(L1)
mostrar_listas(L1,L2)
mostrar_listas1(L1,L2)

a=input("¿Cuál es el extremo izquierdo del intervalo?")
b=input("¿Cuál es el extremo derecho del intervalo?")
n=input("¿Cuántos subintervalos?")
L1 = listaC(a,b,n)
L2 = listaF(L1)
mostrar_listas(L1,L2)

