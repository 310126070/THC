# -*- coding: utf-8 -*-
# Tarea 02
# Moctezuma Soto, Fernando

# Programa que define la altura de una pelota lanzada verticalmente hacia
# arriba cuando su velocidad, dada en m/s, es igual a un tercio de su velocidad de
# lanzamiento.

def altura(v0):
    vf = (1.0/3) * v0
    g = 9.81
    h = (v0**2 - vf**2) / (2*g)
    return(h)
