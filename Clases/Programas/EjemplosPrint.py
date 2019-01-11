# -*- coding: utf-8 -*-

i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
print '"%5d"' % i      # field of width 5 characters
print '"%05d"' % i     # pad with zeros

print '"%g"' % r       # r is big number so this is scientific notation
print '"%G"' % r       # E in the exponent
print '"%e"' % r       # compact scientific notation
print '"%E"' % r       # compact scientific notation
print '"%20.2E"' % r   # 2 decimals, field of width 20
print '"%30g"' % r     # field of width 30 (right-adjusted)
print '"%-30g"' % r    # left-adjust number
print '"%-30.4g"' % r  # 3 decimals

print '%s' % i   # can convert i to string automatically
print '%s' % r

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)


print ''' \n
i = 62
r = 189876545.7654675432

# Imprima números con comillas "" de tal manera que veamos
# ancho del campo
print '% d'% i # campo mínimo
print '% 5d'% i # campo de ancho 5 caracteres
print '% 05d'% i # pad con ceros

print '% g'% r # r es un número grande, así que esta es una notación científica
print '% G'% r # E en el exponente
print '% e'% r # notación científica compacta
print '% E'% r # notación científica compacta
print '% 20.2E'% r # 2 decimales, campo de ancho 20
print '% 30g'% r # campo de ancho 30 (ajustado a la derecha)
print '% -30g'% r # ajuste el número a la izquierda
print '% -30.4g'% r # 3 decimales

print '% s'% i # puede convertir i a cadena automáticamente
print '% s'% r

# Use %% para imprimir el signo de porcentaje
imprimir '% g %% de% .2f Euro es% .2f Euro'% \
      (5.1, 346, 5.1 / 100 * 346)
'''
