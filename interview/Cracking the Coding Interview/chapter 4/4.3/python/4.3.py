class BinaryTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self,data):
        if not self.data:
            self.data = data
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinaryTree(data)

    def inOrder(self):
        if self.left:
            self.left.inOrder()

        if self.data:
            print(str(self.data) + ' ')

        if self.right:
            self.right.inOrder()

    def __str__(self):
        thislevel = [self]
        alllevels = []
        while thislevel:
            nextlevel = []
            
            l = []
            for t in thislevel:
                if t.data:
                    l.append(str(t.data))
                else:
                    l.append(' ')
                if t.left:
                    nextlevel.append(t.left)
                if t.right:
                    nextlevel.append(t.right)

            alllevels.append(l)
            thislevel = nextlevel

        n = len(alllevels)
        S = ''
        for i in range(0,n):
            S += (' '*(n-i)) + (' '*(n-i)).join(alllevels[i]) + '\n'
            
        return S

    def height(self):
        if self.left and self.right:
            return max(self.left.height(), self.right.height()) + 1
        elif self.left:
            return self.left.height() + 1
        elif self.right:
            return self.right.height() + 1
        elif self.data:
            return 1
        else:
            return 0
        
def createBST(arr,T):
    if len(arr) == 0:
        return
    split = len(arr)/2
    T.insert(arr[split])
    if split == 0:
        return
    T.left = BinaryTree()
    createBST(arr[0:split],T.left)
    
    T.right = BinaryTree()
    createBST(arr[split+1:],T.right)

A = [i for i in range(0,10)]

T = BinaryTree()
createBST(A,T)
print(T.height())
print(T)

    
