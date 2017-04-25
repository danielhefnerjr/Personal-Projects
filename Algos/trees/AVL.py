from BST import *
class AVL(BST):
    def __init__(self, key=None, left=None, right=None):
        super().__init__(key,left,right)
        self.balance_factor = (self.left.height() if self.left else 0) - (self.right.height() if self.right else 0)

    def insert(self,key):
        if self.key is None:
            self.key = key
        else:
            if key < self.key:
                if self.left is None:
                    self.left = AVL()
                self.left.insert(key)
                self.left.parent = self
            else:
                if self.right is None:
                    self.right = AVL()
                self.right.insert(key)
                self.right.parent = self
                
        new_balance_factor = (self.left.height() if self.left else 0) - (self.right.height() if self.right else 0)

        if abs(new_balance_factor) == 2:
            self.balance(new_balance_factor)

        self.balance_factor = (self.left.height() if self.left else 0) - (self.right.height() if self.right else 0)

    def delete(self, key):
        if self.key != key:
            if self.key > key:
                self.left.delete(key)
            else:
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

            
        new_balance_factor = (self.left.height() if self.left else 0) - (self.right.height() if self.right else 0)
        
        if abs(new_balance_factor) == 2:
            self.balance(new_balance_factor)
        self.balance_factor = (self.left.height() if self.left else 0) - (self.right.height() if self.right else 0)

            
        

    def balance(self,new_balance_factor):
        # tree is unbalanced, need to rotate
        if new_balance_factor > self.balance_factor:
            # left insertion
            if self.left.balance_factor < 0:
                # left right insertion
                self.left.right.rotate_left()

            # left left insertion
            self.left.rotate_right()
        else:
            # right insertion
            if self.right.balance_factor > 0:
                # right left insertion
                self.right.left.rotate_right()

            # right right insertion
            self.right.rotate_left()

    def rotate_left(self):
        if self.parent.parent:
            temp = self.left
            self.left = self.parent
            self.parent.right = temp

            if self.parent == self.parent.parent.left:
                self.parent.parent.left = self
            else:
                self.parent.parent.right = self

            temp = self.parent.parent
            self.parent.parent = self
            self.parent = temp
        else:
            # if parent is a root node, need to keep root in tact, so move subtrees around
            self.parent.right = self.right
            tmp = self.left
            self.left = self.parent.left
            self.right.parent = self.parent
            self.right = tmp
            
            self.parent.left = self
            
            # then swap keys
            temp = self.parent.key
            self.parent.key = self.key
            self.key = temp
            

    def rotate_right(self):
        

        if self.parent.parent:
            temp = self.right
            self.right = self.parent
            self.parent.left = temp

            if self.parent == self.parent.parent.right:
                self.parent.parent.right = self
            else:
                self.parent.parent.left = self

            temp = self.parent.parent
            self.parent.parent = self
            self.parent = temp
        else:
            self.parent.left = self.left
            tmp = self.right
            self.right = self.parent.right
            self.left.parent = self.parent
            self.left = tmp

            self.parent.right = self
            
            temp = self.parent.key
            self.parent.key = self.key
            self.key = temp
def main():
    # LL insertion
    t = AVL(3, left=AVL(2))
    t.insert(1)
    t.print()
    print('\n'+str(t.balance_factor))
    
    # LR insertion
    t = AVL(3, left=AVL(1))
    t.insert(2)
    t.print()
    print('\n'+str(t.balance_factor))
    
    # RL insertion
    t = AVL(3, right=AVL(5))
    t.insert(4)
    t.print()
    print('\n'+str(t.balance_factor))
    
    # RR insertion
    t = AVL(3, right=AVL(5))
    t.insert(6)
    t.print()
    print('\n'+str(t.balance_factor))

    # LL deletion
    t = AVL(3,left=AVL(2,left=AVL(1)),right=AVL(4))
    t.delete(4)
    t.print()
    print('\n'+str(t.balance_factor))
    
    t = AVL(3,left=AVL(2,left=AVL(1)),right=AVL(4))
    t.delete(3)
    t.print()
    print('\n'+str(t.balance_factor))
    
    # LR deletion
    t = AVL(3,left=AVL(1,right=AVL(2)),right=AVL(4))
    t.delete(4)
    t.print()
    print('\n'+str(t.balance_factor))
    t = AVL(3,left=AVL(1,right=AVL(2)),right=AVL(4))
    t.delete(3)
    t.print()
    print('\n'+str(t.balance_factor))
    
    # RL deletion
    t = AVL(2,left=AVL(1),right=AVL(4,left=AVL(3)))
    t.delete(1)
    t.print()
    print('\n'+str(t.balance_factor))
    
    t = AVL(2,left=AVL(1),right=AVL(4,left=AVL(3)))
    t.delete(2)
    t.print()
    print('\n'+str(t.balance_factor))
    # not working!
    
    # RR deletion
    t = AVL(2,left=AVL(1),right=AVL(4,right=AVL(5)))
    t.delete(1)
    t.print()
    print('\n'+str(t.balance_factor))

    t = AVL(2,left=AVL(1),right=AVL(4,right=AVL(5)))
    t.delete(2)
    t.print()
    print('\n'+str(t.balance_factor))
    # not working!
    
if __name__ == '__main__':
    main()
