def diana(x,y):
    import math
    if ( x < 5 or x >= 25 ) and ( y < 10 or y >= 30 ):
        return (3)
    else:
        if ( x < 5 or x >= 25 ) and ( y >= 10 and y < 30 ):
            return (5)
        else:
            if ( x >= 5 and x < 25 ) and ( y < 10 or y >= 30 ):
                return (7)
            else:
                if pow ( x-15. ,2 ) + pow ( y-20. ,2 ) < 100:
                    return (10)
                else:
                    return (100) 
