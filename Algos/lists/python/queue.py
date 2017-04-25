class Queue:
    def __init__(self,L = None):
        self.q = L or []

    def enqueue(self,x):
        self.q.append(x)

    def dequeue(self):
        ret = self.q[0]
        del self.q[0]
        return ret
    
    def __len__(self):
        return len(self.q)
