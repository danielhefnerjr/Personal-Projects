from itertools import zip_longest

class BinaryTree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinaryTree(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinaryTree(data)
        else:
            self.data = data

    def BFSCompare1(self,root2):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            for n in thislevel:
                if n.data == root2.data:
                    if n.BFSCompare2(root2):
                        return True

                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)
            thislevel = nextlevel

        return False

    def BFSCompare2(self,root2):
        thislevel1 = [self]
        thislevel2 = [root2]

        while thislevel1 and thislevel2:
            nextlevel1 = []
            nextlevel2 = []
            for n1,n2 in zip_longest(thislevel1,thislevel2):
                if not n1 or not n2: return False
                if n1.data != n2.data:
                    return False

                if n1.left: nextlevel1.append(n1.left)
                if n1.right: nextlevel1.append(n1.right)
                if n2.left: nextlevel2.append(n2.left)
                if n2.right: nextlevel2.append(n2.right)

            thislevel1 = nextlevel1
            thislevel2 = nextlevel2

##        print(nextlevel1, nextlevel2)
        if nextlevel1 or nextlevel2:
            return False

        return True


def createBST(arr,T):
    if len(arr) == 0:
        return
    split = int(len(arr)/2)
    T.insert(arr[split])
    if split == 0:
        return
    T.left = BinaryTree()
    createBST(arr[0:split],T.left)
    
    T.right = BinaryTree()
    createBST(arr[split+1:],T.right)
    
B1 = BinaryTree()
B1.insert(3)
B1.insert(1)
B1.insert(0)
B1.insert(2)

B2 = BinaryTree()
B2.insert(1)
B2.insert(0)
B2.insert(2)

print(B1.BFSCompare1(B2))

T2 = BinaryTree()
createBST([i for i in range(0,1000000)],T2)

T1 = BinaryTree(1000001,T2)
print(T1.BFSCompare1(T2))
