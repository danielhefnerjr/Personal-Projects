#.............Problem 5...................
# Needs redoing 
i = 1
while True:
    stop = True
    for j in range(11,21):
        if i % j > 0:
            stop = False
            break
    if stop:
        break
    i += 1

print(i)

