class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self,data):
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

    def height(self):
        if self.left and self.right:
            return max(self.left.height(),self.right.height()) + 1
        elif self.left:
            return self.left.height() + 1
        elif self.right:
            return self.right.height() + 1
        else:
            return 1

    def isBalanced(self):
        if self.left and self.right:
            return abs(self.left.height() - self.right.height()) <= 1
        elif self.left:
            return self.left.height() == 1
        elif self.right:
            return self.right.height() == 1
        else:
            return True

B = BinaryTree(3,BinaryTree(1),BinaryTree(4))
print(B.isBalanced())
        

B = BinaryTree(3,BinaryTree(1,BinaryTree(0)),BinaryTree(4))
print(B.isBalanced())

B = BinaryTree(3,BinaryTree(1,BinaryTree(0,BinaryTree(-1))),BinaryTree(4))
print(B.isBalanced())
