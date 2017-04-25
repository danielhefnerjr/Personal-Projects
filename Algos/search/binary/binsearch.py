''' Binary search on a list '''

def BinSearch(L,x):
    if len(L) == 0:
        return False
    
    if len(L) == 1:
        if L[0] == x:
            return True
        else:
            return False

    n = len(L)
    
    return max(BinSearch(L[0:int(n/2)],x),BinSearch(L[int(n/2):n],x))
