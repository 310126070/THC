def cubos(n):
    if n == 1:
        return 1
    else:
        return n**3 + cubos(n-1)
