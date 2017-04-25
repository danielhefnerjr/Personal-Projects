# http://www.techiedelight.com/inplace-merge-two-sorted-arrays/
def inplace_merge(X,Y):
    i = 0
    while i < len(X):
        if X[i] > Y[0]:
            X[i],Y[0] = Y[0],X[i]
            # bubble up new elem in Y
            j = 0
            while j < len(Y)-1 and Y[j] > Y[j+1]:
                Y[j],Y[j+1] = Y[j+1],Y[j]
                j += 1
        
        i += 1
    
    


X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]

inplace_merge(X,Y)
print(X,Y)