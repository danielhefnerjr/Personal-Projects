class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,x):
        self.stack.append(x)
        
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

class SetOfStacks:
    def __init__(self, maxStackSize = 20):
        self.stacks = [Stack()]
        self.maxStackSize = maxStackSize

    def push(self, x):
        if self.stacks[-1].size() == self.maxStackSize: 
            self.stacks.append(Stack())

        self.stacks[-1].push(x)

    def pop(self):
        x = self.stacks[-1].pop()
        if len(self.stacks) > 1 and self.stacks[-1].size() == 0:
            del self.stacks[-1]
        return x

    def popAt(self,index):
        return self.stacks[index].pop()

    def peek(self):
        return self.stacks[-1].peek()
    
    
S = SetOfStacks(2)
S.push(1)
S.push(2)
S.push(3)
S.push(4)
print(S.pop()) # 4
print(S.popAt(0)) # 2
S.push(4) # 4 
print(S.pop()) # 4 
print(S.pop()) # 3
print(S.pop()) # 1
