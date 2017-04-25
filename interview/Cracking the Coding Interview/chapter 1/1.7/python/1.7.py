import copy

def zero(M):
    m = len(M)
    n = len(M[0])
    N = [row[:] for row in M]
    for i in range(0,m):
        for j in range(0,n):
            if M[i][j] == 0:
                for x in range(0,n):
                    N[i][x] = 0

                for y in range(0,m):
                    N[y][j] = 0
    return N

def zero_inplace(M):
    #M = copy.deepcopy(M)
    cols = []
    rows = []
    m = len(M)
    n = len(M[0])
    for i in range(0,m): # rows
        for j in range(0,n): # cols
            if M[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for r in rows:
        for j in range(0,n):
            M[r][j] = 0
    for c in cols:
        for i in range(0,m):
            M[i][c] = 0

    #return M
                
def set(X):
    X[0] = 7
    
x = [[1,2,3],[0,4,5],[6,7,0]]
print(x)
print(zero(x))
x = [[1,2,3],[0,4,5],[6,7,0]]
zero_inplace(x)
print(x)
