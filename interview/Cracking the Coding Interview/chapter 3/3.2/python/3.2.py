class MinStack:
    def __init__(self):
        self.stack = []
        self.min_history = []

    def push(self,x):
        self.stack.append(x)

        if len(self.min_history) == 0 or x < self.min_history[-1]:
            self.min_history.append(x)
            
    def pop(self):
        if self.stack[-1] == self.min_history[-1]:
            self.min_history.pop()
            
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def get_min(self):
        return self.min_history[-1]


S = MinStack()
S.push(1)
S.push(2)
S.push(0)
S.push(3)
print(S.get_min()) # 0
print(S.pop()) # 3
S.push(4)
S.push(-1)
S.push(5)
print(S.get_min()) # -1
print(S.pop()) # 5
print(S.pop()) # -1
print(S.get_min()) # 0
