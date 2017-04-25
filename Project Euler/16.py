import math

base = 2
power = 1000
num_digits = math.ceil(power * math.log(base,10))

s = 0
for i in reversed(range(1,num_digits)):
    x = 10 ** (power * log(base,10) - (num_digits-1))
    s += int(x)
    
    
