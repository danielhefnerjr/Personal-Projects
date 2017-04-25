def findmagic(A, start, end):
    if end - start == 1:
        if A[start] == start:
            return start
        else:
            return -1

    mid = (end - start) / 2 + start
    return max(findmagic(A, start, mid), findmagic(A,mid,end))

A = [0,1,2,3]
print findmagic(A, 0, len(A))


A = [1,3,2,0]
print findmagic(A, 0, len(A))

A = [4,3,2,3,1]
print findmagic(A, 0, len(A))

A = [4,3,0,5,1]
print findmagic(A, 0, len(A))
