def resolver(L,e):
    print e
    n = len(L[0])
    m = len(L)
    x = e[0]
    y = e[1]
    if y == n-1 or x == m-1:
        return e[0]+1,e[1]+1
    else:
        if L[x][y+1] == False:
            e = [x,y+1]
            return resolver(L,e)
        elif L[x+1][y] == False:
            e = [x+1,y]
            return resolver(L,e)
        else:
            print "No puede continuar avanzando"

L = [[True, True, True, True],
     [False, False, False, True],
     [True, True, False, True]]

type(L)
e = [1,0]
r = resolver(L,e)
import numpy as np
print(np.matrix(L))
