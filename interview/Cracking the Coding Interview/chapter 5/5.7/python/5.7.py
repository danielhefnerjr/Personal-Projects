def ithBit(a,i):
    return ((1 << i) & a) >> i

def findMissing(A,n):
    found = [False for i in range(0,n+1)]
    for a in A:
        x = 0
        for i in reversed(range(0,n.bit_length())):
            x <<= 1
            x = (x | ithBit(a,i))

        found[x] = True

    for i in range(0,n+1):
        if found[i] == False:
            return i

n = 32
missing = 27

A = [i for i in range(0,missing)] + [i for i in range(missing+1,n+1)]
print(findMissing(A,n))
        
