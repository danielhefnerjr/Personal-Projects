def makeChange(goal,denom):
    if denom == 1:
        return 1
    
    next_denom = {
            25: 10,
            10: 5,
            5: 1
        }[denom]

    ways = 0
    for i in range(goal/denom + 1):
        ways += makeChange(goal-i*denom,next_denom)

    return ways

print(makeChange(125,25))
