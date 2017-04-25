def waysToReach(x,y):
    if (x,y) == (0,0):
        return 0
    if (x,y) == (1,0):
        return 1
    if (x,y) == (0,1):
        return 1
    
    ways = 0
    if x > 0:
        ways += waysToReach(x-1,y)
    if y > 0:
        ways += waysToReach(x,y-1)

    return ways

print(waysToReach(0,1))
print(waysToReach(1,0))
print(waysToReach(1,1))
print(waysToReach(2,0))
print(waysToReach(2,1))
