from importlib.machinery import SourceFileLoader

BST = SourceFileLoader('BST','../../trees/BST.py').load_module()
Queue = SourceFileLoader("Queue",'../../lists/queue.py').load_module()

Q = Queue.Queue()

def BFS(T,x):
    global Q
    
    if T.key == x:
        return True

    if T.left:
        Q.enqueue(T.left)

    if T.right:
        Q.enqueue(T.right)

    if len(Q) == 0:
        return False

    return BFS(Q.dequeue(),x)
