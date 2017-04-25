#.............Problem 4...................
max_x = -float('inf')
for i1 in range(100,1000):
    for i2 in range(100,1000):
        x = i1*i2
        if str(x) == str(x)[-1::-1] and x > max_x:
            max_x = x

print(max_x)
