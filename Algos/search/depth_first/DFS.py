from importlib.machinery import SourceFileLoader

BST = SourceFileLoader('BST','../../trees/BST.py').load_module()

def DFS(T,x):
    if T.key == x:
        return True

    if T.left and T.right:
        return max(DFS(T.left,x),DFS(T.right,x))
    elif T.left:
        return DFS(T.left,x)
    elif T.right:
        return DFS(T.right,x)
    else:
        return False
