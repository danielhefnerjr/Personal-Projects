class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self,data):
        n = Node(data,self.head)
        self.head = n

    def isEmpty(self):
        return not self.head

    def pr(self):
        curr = self.head

        print(curr.data.data)
        curr = curr.next
        
        while curr:
            print('| ' + str(curr.data.data))
            curr = curr.next

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

    def createLists(self):
        l = LinkedList(Node(self))
        lists = []

        while not l.isEmpty():
            lists.append(l)
            next_l = LinkedList()
            l_curr = l.head
            while l_curr:
                t = l_curr.data
                if t.left:
                    next_l.insert(t.left)
                if t.right:
                    next_l.insert(t.right)
                l_curr = l_curr.next
            l = next_l
        return lists

b = BinaryTree(3)
b.insert(1)
b.insert(0)
b.insert(2)
b.insert(5)
b.insert(4)
b.insert(6)
lists = b.createLists()
for l in lists:
    l.pr()
