def mergesort(L):
    l = len(L)
    if l <= 1:
        return L

    return merge(mergesort(L[:int(l/2)]),mergesort(L[int(l/2):]))

def merge(L1,L2):
    L = []
    l1 = len(L1)
    l2 = len(L2)
    i = 0
    j = 0
    for k in range(0,l1+l2):
        if i < l1 and (j >= l2 or L1[i] < L2[j]):
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1


    return L


def main():
    x = [4,3,2,1]
#    assert([1,2,3,4] == mergesort(x))
    print(mergesort(x))
if __name__ == '__main__':
    main()
