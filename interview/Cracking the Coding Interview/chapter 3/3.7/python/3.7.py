class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def insert(self,data):
        n = Node(data, self.head)
        
        if not self.head:
            self.tail = n
            
        self.head = n

    def search(self,data):
        curr_node = self.head
        while curr_node and curr_node.data != data:
            curr_node = curr_node.next_node

        return curr_node
        
    def removeFirst(self,data):
        
        curr_node = self.head
        prev_node = None
        while curr_node and curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next_node

        if curr_node:
            if curr_node == self.head:
                self.head = curr_node.next_node
            else:
                prev_node.next_node = curr_node.next_node
        else:
            raise ValueError('Value not in list')

    def removeAt(self,ind):
        curr_node = self.head
        prev_node = None
        i = 0
        while curr_node and i < ind:
            prev_node = curr_node
            curr_node = curr_node.next_node
            i += 1

        if curr_node:
            if curr_node == self.head:
                self.head = curr_node.next_node
            else:
                prev_node.next_node = curr_node.next_node
        else:
            raise IndexError('Index out of list bounds')

    def __len__(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next_node

        return count
        
    def isEmpty(self):
        return not self.head

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self,pet):
        self.list.insert(pet)

    def dequeueAny(self):
        ret = self.list.head.data
        self.list.removeAt(len(self.list)-1)

    def dequeueDog(self):
    
