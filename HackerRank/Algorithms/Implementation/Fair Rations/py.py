#!/bin/python3

import sys


N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

if len(B) <= 1 or sum(b % 2 == 1 for b in B) % 2 == 1:
    print('NO')
else:
    c = 0
    while sum(b % 2 == 1 for b in B) > 0:
        i = next(B.index(b) for b in B if b % 2 == 1)
        B[i] += 1
        B[i+1] += 1
        c += 2
    print(c)