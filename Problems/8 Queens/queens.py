def placequeens(row, placed):
    if row > 8:
        print(placed)
        return True
    
    for col in range(1,9):
        if isvalid(row,col,placed):
            if placequeens(row+1,placed + ((row,col),)):
                return True
        
    return False

def isvalid(row,col,placed):
    for q in placed:
        if q[0] == row or q[1] == col or q[1]-q[0] == col-row or (9-q[1])-q[0] == (9-col)-row:
            return False
        
    return True
    
placequeens(1,())