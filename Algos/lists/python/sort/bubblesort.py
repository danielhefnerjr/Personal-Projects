def bubblesort(L):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0,len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True

    return L

def main():
    bubblesort([4,3,2,1])

if __name__ == '__main__':
    main()
    
