def setBit(x,i):
    return x | (1 << i)

def drawHorizontalLine(screen, width, x1, x2, y):
    for w in range(x1,x2+1):
        byte = width/8*y + int(w/8)
        bit = width*y + w - byte*8
##        print(byte,bit,w)

        screen[byte] = setBit(screen[byte],bit)


screen = [0] * 20 # 16x10
drawHorizontalLine(screen,16,1,10,3)
for b in screen:
    print(bin(b))
