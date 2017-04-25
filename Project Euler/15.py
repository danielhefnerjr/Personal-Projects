#.......Problem 15........
M = 20
N = 20
lookup = [[0]*(N+1)]*(M+1)
for i in range(1,M+1):
    lookup[i][0] = 1
for i in range(1,N+1):
    lookup[0][i] = 1
    
for i in range(1,M+1):
    for j in range(1,N+1):
        lookup[i][j] = lookup[i-1][j] + lookup[i][j-1]

print(lookup[M][N])
