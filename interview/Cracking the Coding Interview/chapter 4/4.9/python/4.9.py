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

    def DFS1(self,target):
        if self.data == target:
            print([self.data])
            return

        if self.left:
            self.left.DFS2(target,self.data,[self.data])

        if self.right:
            self.right.DFS2(target,self.data,[self.data])
        

    def DFS2(self,target,S,path):
        S += self.data
        path = path + [self.data]

        if S == target:
            print(path)
            return
        
        if S > target:
            return

        if self.left:
            self.left.DFS2(target,S,path)

        if self.right:
            self.right.DFS2(target,S,path)

B = BinaryTree(3,BinaryTree(1,BinaryTree(5),BinaryTree(2)),BinaryTree(5,BinaryTree(4),BinaryTree(1)))

B.DFS1(9)
        
