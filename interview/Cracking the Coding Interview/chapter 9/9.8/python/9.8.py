
def countWays(goal, quarters,dimes,nickels,pennies, ways):
    global nways
    
    current = 25*quarters + 10*dimes + 5*nickels + pennies
    if current > goal:
        return ways
    
    if nways[quarters][dimes][nickels][pennies] > 0:
##        print(quarters,dimes,nickels,pennies,ways)
        return ways
        
    if current == goal:
##        print(current,quarters,dimes,nickels,pennies)
        nways[quarters][dimes][nickels][pennies] = 1
        return ways + 1

    return countWays(goal,quarters+1,dimes,nickels,pennies, ways) \
           + countWays(goal,quarters,dimes+1,nickels,pennies, ways)  \
           + countWays(goal,quarters,dimes,nickels+1,pennies, ways) \
           + countWays(goal,quarters,dimes,nickels,pennies+1, ways)


n = 25

maxquarters = n/25
maxdimes = n/10
maxnickels = n/5
maxpennies = n

nways = [[[[0 for p in range(maxpennies+1)] for c in range(maxnickels+1)] for d in range(maxdimes+1)] for q in range(maxquarters+1)]
print(countWays(n,0,0,0,0,0))
