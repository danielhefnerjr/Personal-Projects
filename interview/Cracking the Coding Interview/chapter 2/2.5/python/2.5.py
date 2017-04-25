class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def __len__(self):
        return self.size()

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def __contains__(self, data):
        return self.search(data)
        
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")
        if previuos is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        s = ''
        current = self.head
        while current:
            s += str(current.get_data()) + ','
            current = current.get_next()
        return s[:-1]

def add(n1, n2):
    S = LinkedList()
    curr_S = None
    curr_n1 = n1.head
    curr_n2 = n2.head

    carry = 0
    while curr_n1 != None and curr_n2 != None:
        s = curr_n1.get_data() + curr_n2.get_data() + carry
        
        if curr_S == None:
            S.insert(s % 10)
            curr_S = S.head
        else:
            N = Node(s % 10)
            curr_S.set_next(N)
            curr_S = N
            
        carry = int(s/10)
        
        curr_n1 = curr_n1.get_next()
        curr_n2 = curr_n2.get_next()

    if curr_n1 == None:
        while curr_n2 != None:
            s = curr_n2.get_data() + carry
            N = Node(s % 10)
            curr_S.set_next(N)
            curr_S = N
            carry = int(s/10)
            
            curr_n2 = curr_n2.get_next()
            
    elif curr_n2 == None:
            s = curr_n1.get_data() + carry
            N = Node(s % 10)
            curr_S.set_next(N)
            curr_S = N
            carry = int(s/10)
        
            curr_n1 = curr_n1.get_next()
            
    if carry > 0:
        curr_S.set_next(Node(carry))
        
    return S
##
##def add_forward(n1, n2):
##    S = LinkedList()
##    curr_S = None
##    curr_n1 = n1.head
##    curr_n2 = n2.head
##
##    carry = 0
##    while curr_n1 != None and curr_n2 != None:
##        s = curr_n1.get_data() + curr_n2.get_data() + carry
##        
##        S.insert(s % 10)            
##        carry = int(s/10)
##        
##        curr_n1 = curr_n1.get_next()
##        curr_n2 = curr_n2.get_next()
##
##    if curr_n1 == None:
##        while curr_n2 != None:
##            s = curr_n2.get_data() + carry
##            N = Node(s % 10)
##            curr_S.set_next(N)
##            curr_S = N
##            carry = int(s/10)
##            
##            curr_n2 = curr_n2.get_next()
##            
##    elif curr_n2 == None:
##            s = curr_n1.get_data() + carry
##            N = Node(s % 10)
##            curr_S.set_next(N)
##            curr_S = N
##            carry = int(s/10)
##        
##            curr_n1 = curr_n1.get_next()
##            
##    if carry > 0:
##        curr_S.set_next(Node(carry))
##        
##    return S

# 123 + 123 = 246
L1 = LinkedList(Node(3,Node(2,Node(1))))
L2 = LinkedList(Node(3,Node(2,Node(1))))
print(add(L1,L2))

# 617 + 295 = 912
L1 = LinkedList(Node(7,Node(1,Node(6))))
L2 = LinkedList(Node(5,Node(9,Node(2))))
print(add(L1,L2))

# 717 + 295 = 1012
L1 = LinkedList(Node(7,Node(1,Node(7))))
L2 = LinkedList(Node(5,Node(9,Node(2))))
print(add(L1,L2))

# 123 + 1081 = 1204
L1 = LinkedList(Node(3,Node(2,Node(1))))
L2 = LinkedList(Node(1,Node(8,Node(0,Node(1)))))
print(add(L1,L2))
