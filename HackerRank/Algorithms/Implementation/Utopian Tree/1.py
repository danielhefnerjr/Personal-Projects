#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    h = 1
    for i in range(n):
        if i % 2 == 1: # starting at i = 0
            h += 1
        else:
            h *= 2
    print(h)