class BinaryTree:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinaryTree(data,parent=self)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinaryTree(data,parent=self)
        else:
            self.data = data

    def findSuccessor(self,data=None):
        if data is None:
            data = self.data

        if self.data > data:
            if self.left:
                s = self.left.findSuccessor(data)
                if s is None:
                    return self
                else:
                    return s
            else:
                return self
        else:
            if self.right:
                return self.right.findSuccessor(data)
            else:
                if self.parent.data > data:
                    return self.parent
                else:
                    return None
    

B = BinaryTree(3)
B.insert(1)
B.insert(4)
B.insert(0)
B.insert(2)
B.insert(5)
B.insert(6)
print(B.findSuccessor(0).data)
print(B.findSuccessor(1).data)
print(B.findSuccessor(2).data)
print(B.findSuccessor(3).data)
print(B.findSuccessor(4).data)
print(B.findSuccessor(5).data)
print(B.findSuccessor(6).data)
