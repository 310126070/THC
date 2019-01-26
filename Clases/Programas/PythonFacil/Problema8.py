def g(1):
    a = 0

    for i in 1:
        for j in 1:
            if abs(i-j) > a:
                a = abs(i-j)
                
    return a 
