def isSubstring(s1, s2):
    return s1 in s2

def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False

    return isSubstring(s1, s2+s2)
