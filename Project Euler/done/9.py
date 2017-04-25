#.............Problem 9...................
# c = sqrt(a^2 + b^2)
# c = 1000 - a - b

import math

for a in range(1,1000):
    for b in range(1,1000):
        if math.sqrt(a**2 + b**2) == 1000 - a - b:
            c = 1000 - a - b
            print(a*b*c)
            quit()
