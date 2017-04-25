def stuff(N,M,i,j):
    # clear bits i through j of N
    # shift M over i
    # or N and M
    return (N & (~(((1 << j)-1)) << i)) | (M << i)


N = int('10000000000',2)
M = int('10011',2)
print('{0:b}'.format(stuff(N,M,2,6)))
