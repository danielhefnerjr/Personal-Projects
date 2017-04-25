#.............Problem 2...................
f1 = 1
f2 = 1
s = 0
while True:
    f3 = f1 + f2
    if f3 >= 4000000:
        break
    if f3 % 2 == 0:
        s += f3
    f1 = f2
    f2 = f3

print(s)