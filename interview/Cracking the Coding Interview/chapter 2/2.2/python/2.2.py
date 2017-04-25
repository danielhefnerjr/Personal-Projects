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

    def kth_to_last_elem(self,k):
        N = len(self)
        if k > N:
            raise IndexError('k too large')
        n = N-k
        current = self.head
        i = 0
        while i < n:
            current = current.get_next()
            i += 1

        return current.get_data()
        

L = LinkedList()
L.insert(5)
L.insert(4)
L.insert(3)
L.insert(2)
L.insert(1)
L.insert(0)
L.kth_to_last_elem(3)
