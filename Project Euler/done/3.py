import math
#.............Problem 3...................
n = 600851475143
sqrt_n = int(math.sqrt(n))
# Sieve of Eratosthenes
primes = [1]*sqrt_n
i = 2
while i < sqrt_n:
    j = i*2
    while j < sqrt_n:
        primes[j] = 0
        j += i
    i += 1

max_i = -float('inf')
i = 2
while i < sqrt_n:
    if n % i == 0 and primes[i] and i > max_i:
        max_i = i
    i += 1

print(max_i)
