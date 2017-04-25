import math

n = 100

log_n_fact = 0
for i in range(1,n+1):
    log_n_fact += math.log(i, 10)

max_pow = int(log_n_fact)
S = 0
x = 10**(log_n_fact-int(max_pow))
S += x
x -= int(x)
for i in reversed(range(1,max_pow)):
    x *= 10
    S+= int(x)
    x -= int(x)


#sum([int(x) for x in str(math.factorial(100))])
