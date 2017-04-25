# http://www.techiedelight.com/find-index-0-replaced-get-maximum-length-sequence-of-continuous-ones/
def search(X):
    zeros = [0]
    for i,x in enumerate(X):
        if x == 0:
            zeros.append(i)

    #zeros.insert(0, zeros[0])
    zeros.append(len(X))
    
    m = float('-inf')
    for i in range(1, len(zeros)-1):
        m = max(m, zeros[i+1]-zeros[i-1])
        
    return m    

X = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1,0]
print(search(X))