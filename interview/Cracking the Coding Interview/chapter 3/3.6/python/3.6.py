class Stack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack

def sortStack(S1):
    S2 = Stack()
    # count items
    n = 0
    while not S1.isEmpty():
        S2.push(S1.pop())
        n += 1

    # move back

    while not S2.isEmpty():
        S1.push(S2.pop())

    n1 = n
    # after n times of pushing min of (n-1), (n-2), ... , items on S1,
    # S1 should be sorted in ascending order
    for i in range(0,n):
        min_x = float('inf')
        # move from S1 to S2, store min
        for j in range(0,n1):
            x = S1.pop()
            
            if x < min_x:
                min_x = x

            S2.push(x)
            
        # put min on S1
        S1.push(min_x)

        # working with one less item now
        n1 -= 1
        
        # move from S2 to S1
        while not S2.isEmpty():
            x = S2.pop()
            if x != min_x:
                S1.push(x)

    return S1

S = Stack()
S.push(3)
S.push(1)
S.push(2)
print(S.stack)
S = sortStack(S)
print(S.stack)
        

        
        
