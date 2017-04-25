def countbits(x):
    n = 0
    while x:
        x &= x-1
        n += 1
    return n

def numchangebits(x,y):
    return abs(countbits(x)-countbits(y))

print(numchangebits(31,14))
