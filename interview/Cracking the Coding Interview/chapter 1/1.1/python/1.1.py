def allUnique(x):
    counts = {}
    for a in x:
        if a in counts:
            counts[a] += 1
        else:
            counts[a] = 1

    for c in counts.values():
        if c > 1:
            return False

    return True


def allUnique_noDataStr(x):
    for i in range(len(x)):
        a = x[i]

        for j in range(i+1,len(x)):
            b = x[j]

            if a == b:
                return False

    return True
