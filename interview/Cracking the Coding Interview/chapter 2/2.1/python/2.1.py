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
    
    def remove_duplicates(self):
        values = []
        current = self.head
        previous = None
        while current:
            if current.get_data() in values:
                previous.set_next(current.get_next())
            else:
                values.append(current.get_data())
                previous = current
            current = current.get_next()
            
    def remove_duplicates_nobuff(self):
        current = self.head
        previous = None
        while current:
            data = current.get_data()

            current2 = current.get_next()
            previous2 = current
            while current2:
                if current2.get_data() == data:
                    previous2.set_next(current2.get_next())
                else:
                    previous2 = current2
                current2 = current2.get_next()

            previous = current
            current = current.get_next()

