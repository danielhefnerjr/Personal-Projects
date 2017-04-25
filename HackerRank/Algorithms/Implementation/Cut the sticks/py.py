#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while any(arr):
    c = len(arr)
    m = min(arr)
    arr = list(filter(lambda x: x, map(lambda x: x-m,arr)))
    print(c)