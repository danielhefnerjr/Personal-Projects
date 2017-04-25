##def subsets(S):
##    if len(S) == 1:
##        return S
##
##    P = [S]
##    for i in range(0,len(S)):
##        P.append(subsets(S[:i] + S[i+1:]))
##
##    return P

def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result
