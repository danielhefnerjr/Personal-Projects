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

def delete_mid_node(N):
    N.data = N.get_next().get_data()
    N.set_next(N.get_next().get_next())


L = LinkedList(Node(1,Node(2,Node(3,Node(4)))))
delete_mid_node(L.search(3))
print(L)
