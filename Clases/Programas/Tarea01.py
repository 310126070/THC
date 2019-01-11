# -*- coding: utf-8 -*-
# Tarea 01
# Moctezuma Soto, Fernando

# Programa que calcula la altura de una pelota lanzada verticalmente hacia
# arriba cuando su velocidad es igual a un tercio de su velocidad de
# lanzamiento, que es de 28 m/s.

v0 = 28

vf = (1.0/3) * v0

g = 9.81

h = (v0**2 - vf**2) / (2*g)

print h

