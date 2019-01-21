def listaC(Cmin, Cmax, n):
    gradosC = []
    dC = (Cmax - Cmin) / float(n-1)
    for i in range(n):
        C = Cmin + i*dC
        gradosC.append(C)
    return gradosC

'''
>>> q=listaC(-12.3,35.8,12)
>>> q
>>> len(q)
'''

def listaF(gradosC):
    gradosF = []
    for C in gradosC:
        F = (9.0/5)*C + 32
        gradosF.append(F)
    return gradosF

def mostrar_listas(gradosC, gradosF):
    for i in range(len(gradosC)):
        C = gradosC[i]
        F = gradosF[i]
        print "%5.1f %5.1f" % (C, F)

        
'''
>>> for i in range(len)(L1)):
        L1[1] += 5
        print C

>>> for i,c in enumerate(L1):
        L1[i] = c + 5
        print i, c

>>> gradosF = [ (9/5.0)*C + 32 for C in grados C ]
>>> gradosF 

>>> C_mas_7 = [ C+5 for C in gradosC ]
>>> C_mas_7
'''

def mostrar_listas1(gradosC, gradosF):
    for C, F in zip(gradosC, gradosF):
        print "%5d %5.1f" % (C, F)


