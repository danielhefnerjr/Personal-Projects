#.............Problem 10..................
import math
limit = 2000000
crosslimit = math.sqrt(limit)
sieve = [1 for x in range(0,limit)]
sieve[0] = 0
sieve[1] = 1
for i in range(2,int(crosslimit)):
    if sieve[i] == 1:
        j = i
        while i*j < limit:
    ##        print(i,j,i*j)
            sieve[i*j] = 0
            j = j + 1
    
print(sum([i for i in range(2,len(sieve)) if sieve[i] == 1]))
