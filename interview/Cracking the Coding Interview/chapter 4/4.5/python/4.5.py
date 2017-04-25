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

    def isBST(self):
        if self.left:
            if self.left.findmax() > self.data or not self.left.isBST():
                return False

        if self.right:
            if self.right.findmin() < self.data or not self.right.isBST():
                return False

        return True

    def findmin(self):
        if self.left and self.right:
            return min(self.data,self.left.findmin(),self.right.findmin())
        elif self.left:
            return min(self.data,self.left.findmin())
        elif self.right:
            return min(self.data,self.right.findmin())
        else:
            return self.data

    def findmax(self):
        if self.left and self.right:
            return max(self.data,self.left.findmax(),self.right.findmax())
        elif self.left:
            return max(self.data,self.left.findmax())
        elif self.right:
            return max(self.data,self.right.findmax())
        else:
            return self.data

b = BinaryTree(3,BinaryTree(1,BinaryTree(0),BinaryTree(2)),BinaryTree(5,BinaryTree(4),BinaryTree(6)))
print(b.isBST()) # true

b = BinaryTree(5,BinaryTree(1,BinaryTree(0),BinaryTree(2)),BinaryTree(5,BinaryTree(4),BinaryTree(6)))
print(b.isBST()) # false


b = BinaryTree(3,BinaryTree(2,BinaryTree(0),BinaryTree(1)),BinaryTree(5,BinaryTree(4),BinaryTree(6)))
print(b.isBST()) # false
