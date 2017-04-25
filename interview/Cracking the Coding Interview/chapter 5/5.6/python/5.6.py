def swapoddsandevens(x):
    mask = 0b10101010101010101010101010101010
    return ((x << 1) & mask) | ((x >> 1) & (mask >> 1))


print(bin(swapoddsandevens(0b1010)))
print(bin(swapoddsandevens(0b0101)))
print(bin(swapoddsandevens(0b111101)))
