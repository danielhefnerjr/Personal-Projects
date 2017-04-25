Ways = [0] + [-1 for i in range(0,1000)]
def waysToClimb(nstairs):
    if nstairs == 0:
        return 0
    if nstairs == 1:
        return 1
    if nstairs == 2:
        return 2
    if nstairs == 3:
        return 4

    if Ways[nstairs] != -1:
        return Ways[nstairs]
    
    ways = 0
    ways += waysToClimb(nstairs-1)
    if nstairs > 1:
        ways += waysToClimb(nstairs-2)

    if nstairs > 2:
        ways += waysToClimb(nstairs-3)

    Ways[nstairs] = ways
    
    return ways



print(waysToClimb(1))
print(waysToClimb(2))
print(waysToClimb(3))
print(waysToClimb(4))
        
    
