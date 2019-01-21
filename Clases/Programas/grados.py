def listaC(Cmin, Cmax, n):
    gradoC = []
    dC = (Cmax - Cmin) / float(n-1)
    for i in range(n):
        C = Cmin + i*dC
        gradosC.append(C)
    return gradosC
