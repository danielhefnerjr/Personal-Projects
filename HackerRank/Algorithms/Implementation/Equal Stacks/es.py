#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

H1 = sum(h1)
H2 = sum(h2)
H3 = sum(h3)

while not (H1 == H2 == H3):
    while H1 > H2 or H1 > H3:
        h = h1.pop(0)
        H1 -= h
    while H2 > H1 or H2 > H3:
        h = h2.pop(0)
        H2 -= h
    while H3 > H1 or H3 > H2:
        h= h3.pop(0)
        H3 -= h
print(H1)