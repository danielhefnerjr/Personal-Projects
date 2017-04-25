def compress(S):
    compressed = ''
    i = 0
    while i < len(S):
        a = S[i]
        c = 1
        
        i += 1
        
        while i < len(S) and S[i] == a:
            c += 1
            i += 1

        compressed += a + str(c)

    if len(S) < len(compressed):
        return S
    else:
        return compressed

