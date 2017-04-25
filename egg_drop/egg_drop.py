max_e = 10
max_k = 1000

MinDrops = [[0 for e in range(0,max_e+1)] for k in range(0,max_k+1)]
MinDrops[1] = [1]*(max_e+1)

for n in range(1,max_k+1):
    MinDrops[n][1] = n

for e in range(2,max_e+1):
    for k in range(2,max_k+1):
        minDrops = float('inf')
        minFloor = 0
        for n in range(2,k+1):
            drops = max(MinDrops[n-1][e-1],MinDrops[k-n][e]) + 1
            if drops < minDrops:
                minDrops = drops
                minFloor = n
        
        MinDrops[k][e] = minDrops
