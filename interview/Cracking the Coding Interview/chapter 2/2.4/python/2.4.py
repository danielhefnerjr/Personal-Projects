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

    def __repr__(self):
        return str(self.data)
    
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

    def partition(self,x):
        X = self.search(3)
        after_X = False
        prev = None
        i = self.head
        while i != None:
            nxt = i.get_next()
            nxt_prev = i
            if i != X:
                if after_X and i.get_data() < X.get_data():
                    prev.set_next(i.get_next())
                    nxt_prev = i.get_next()
                    i.set_next(self.head)
                    self.head = i
                elif not after_X and i.get_data() > X.get_data():
                    if i == self.head:
                        self.head = nxt
                        nxt_prev = None
                    else:
                        prev.set_next(i.get_next())
                        nxt_prev = i.get_next()
                        
                    i.set_next(X.get_next())
                    X.set_next(i)
                    
                        
            else:
                after_X = True
                
            i = nxt
            prev = nxt_prev

# test when X=3 in middle of list
L = LinkedList(Node(5,Node(1,Node(3,Node(2,Node(4))))))
L.partition(3)
print(L)

# test when X=3 head of list
L = LinkedList(Node(3,Node(2,Node(5,Node(1,Node(4))))))
L.partition(3)
print(L)

# test when X=3 tail of list
L = LinkedList(Node(1,Node(5,Node(2,Node(4,Node(3))))))
L.partition(3)
print(L)
