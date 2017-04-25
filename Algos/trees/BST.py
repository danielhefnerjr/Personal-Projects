class BST:
    def __init__(self,key=None,left=None,right=None):
        self.key = key
        self.parent = None
        self.left = left
        if self.left:
            self.left.parent = self
        self.right = right
        if self.right:
            self.right.parent = self

    def search(self,key):
        if self.key == key:
            return self
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(key)

    def insert(self,key):
        if self.key is None:
            self.key = key
        else:
            if key < self.key:
                if self.left is None:
                    self.left = BST()
                self.left.insert(key)
                self.left.parent = self
            else:
                if self.right is None:
                    self.right = BST()
                self.right.insert(key)
                self.right.parent = self

    def delete(self,key):
        if key < self.key:
            self.left.delete(key)
        elif key > self.key:
            self.right.delete(key)
        else:
            if self.right: # node has at least a right child
                # get in order successor (find min of right sub)
                successor = self.right
                while successor.left:
                    successor = successor.left
                # replace self with successor and delete successor node
                self.key = successor.key
                successor.delete(successor.key)
            elif self.left: # node has one child (left)
                # replace with predecessor node
                predecessor = self.left
                while predecessor.right:
                    predecessor = predecessor.right

                self.key = predecessor.key
                predecessor.delete(predecessor.key)
            else:
                if self.parent:
                    if self == self.parent.left:
                        self.parent.left = None
                    else:
                        self.parent.right = None
                else:
                    self.key = None

    def verify(self,minKey,maxKey):
        if self.key < minKey or self.key > maxKey:
            return False
        if self.left and self.right:
            return self.left.verify(minKey, self.key) and self.right.verify(self.key, maxKey)
        elif self.right:
            return self.right.verify(self.key, maxKey)
        elif self.left:
            return self.left.verify(minKey, self.key)
        else:
            return True

    def traverse(self,callback):
        if self.left:
            self.left.traverse(callback)

        callback(self.key)

        if self.right:
            self.right.traverse(callback)

    def height(self):
        if self.left is None and self.right is None:
            return 1
        else:
            return max(self.left.height() if self.left else 0, self.right.height() if self.right else 0) + 1

    def print(self):
        self.traverse(lambda x: print(x, ' ', end=''))

def main():
    t = BST()
    t.insert(30)
    t.insert(10)
    t.insert(20)
    assert t.search(30) is not None
    assert t.search(10) is not None
    assert t.search(20) is not None
    assert t.verify(float('-inf'),float('inf'))
    t.delete(20)
    assert t.search(20) is None
    
    t = BST(20,BST(10), BST(30, BST(5),BST(40)))
    assert t.verify(float('-inf'),float('inf')) == False
    
    t = BST(20,BST(10, None, BST(15)), BST(30, BST(25),BST(40)))
    t.traverse(lambda x: print(x,'',end=''))
    print()
    t.delete(10)
    t.traverse(lambda x: print(x,'',end=''))
    print()
    t.delete(30)
    t.traverse(lambda x: print(x,'',end=''))
    print()

if __name__ == '__main__':
    main()
