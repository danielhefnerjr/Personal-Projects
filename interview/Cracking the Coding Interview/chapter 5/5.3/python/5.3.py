def updateBits(n,i,j,v):
    mask = ~(((1 << (j-i+1))-1) << i)
    return (n & mask) | (v << i)

def findBits(n,v,num_bits):
    for i in range(0,n.bit_length()):
        if n == updateBits(n,i,i+num_bits-1,v):
            return i

    return -1

def nextLargest(n):
    i = findBits(n,0b01,2)
    return updateBits(n,i,i+1,0b10)

def nextSmallest(n):
    i = findBits(n,0b10,2)
    return updateBits(n,i,i+1,0b01)

print(bin(nextLargest(0b11011)))
print(bin(nextSmallest(0b11011)))
