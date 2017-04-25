def mult(x,y):
    i = 0
    s = 0
    while i < y:
        s += x
        i += 1

    return s


def sub(x,y):
    diff = 0
    while y < x:
        y += 1
        diff += 1

    return diff


def div(x,y):
    quot = 1
    while y < x:
        y += y
        quot += 1

    return quot


print(mult(3,4))
print(sub(5,3))
print(div(21,7))
