def rotate(M):
    n = len(M)
    M1 = [[0 for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            M1[i][j] = M[(n-1)-j][i]

    return M1
