def permutations(S):
    perms(S,S,'')

def perms(S, rem, s):
    if len(s) == len(S):
        print(s)
        return

    for i in range(0,len(rem)):
        perms(S, rem[:i]+rem[i+1:], s+rem[i])

permutations('abcd')
