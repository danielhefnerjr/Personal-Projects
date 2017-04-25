def findline(p1,w1,p2,w2):
    x1,y1 = p1
    x2,y2 = p2

    cx1,cy1 = x1 + w1/2, y1 + w1/2
    cx2,cy2 = x2 + w2/2, y2 + w2/2

    m = (cy2-cy1)/(cx2-cx1)
    b = cy2 - m*cx2

    return m,b


