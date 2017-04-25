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

    def search(self,data):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            for n in thislevel:
                if n.data == data:
                    return n
                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)

            thislevel = nextlevel

        return None

    def CommonAncestor_noparents(self,node1,node2):
        sl1 = False
        sl2 = False
        sr1 = False
        sr2 = False
        if self.left:
            sl1 = self.left.contains(node1)
            sl2 = self.left.contains(node2)
            
        if self.right:
            sr1 = self.right.contains(node1)
            sr2 = self.right.contains(node2)

        if sl1 and sl2:
            s = self.left.CommonAncestor_noparents(node1,node2)
            if not s:
                return self
            else:
                return s

        if sr1 and sr2:
            s = self.right.CommonAncestor_noparents(node1,node2)
            if not s:
                return self
            else:
                return s

        if (sl1 and sr2) or (sl2 and sr1):
            return self

        
        return None
        
        

    def contains(self,node):
        if self.data == node.data:
            return True

        if self.left and self.left.contains(node):
            return True

        if self.right and self.right.contains(node):
            return True

        return False

def CommonAncestor(node1,node2):
    parent1 = node1.parent
    while parent1:
        parent2 = node2.parent
        while parent2:
            if parent1 == parent2:
                return parent1
            parent2 = parent2.parent
        parent1 = parent1.parent

    return None

B = BinaryTree(3)
B.insert(1)
B.insert(5)
B.insert(0)
B.insert(2)
B.insert(4)
B.insert(6)
print(CommonAncestor(B.search(0),B.search(4)).data) # 3
print(CommonAncestor(B.search(2),B.search(0)).data) # 1
print(CommonAncestor(B.search(5),B.search(4)).data) # 3
print(CommonAncestor(B.search(2),B.search(0)).data) # 1

print(B.CommonAncestor_noparents(B.search(0),B.search(4)).data) # 3
print(B.CommonAncestor_noparents(B.search(2),B.search(0)).data) # 1
print(B.CommonAncestor_noparents(B.search(5),B.search(4)).data) # 3
print(B.CommonAncestor_noparents(B.search(2),B.search(0)).data) # 1
