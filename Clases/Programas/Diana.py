def diana(x, y):
    if (x<5 and (y<10 or y>30)) or (x>25 and (y<10 or y>30)):
        return (3)
    else:
        if (x<5 or x>25) and (y>10 and y>30):
            return (5)
        else:
            if (x>5 and x<25) and (y<10 or y>30):
                return (7)
            else:
                return (10)
