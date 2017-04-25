def isPermutation(s1, s2):

    if len(s1) != len(s2):
        return False
    
    for a in s1:

        found = False
        for b in s2:
            if a == b:
                if found:
                    return False
                else:
                    found = True

        if not found:
            return False

    return True
