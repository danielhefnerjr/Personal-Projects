class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
        self.stack1.append(x)
        
    def dequeue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        ret = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return ret
            
    def peek(self):
        return self.stack1[-1]


Q = MyQueue()
Q.enqueue(0)
Q.enqueue(1)
print(Q.dequeue()) # 0
Q.enqueue(2)
print(Q.dequeue()) # 1
