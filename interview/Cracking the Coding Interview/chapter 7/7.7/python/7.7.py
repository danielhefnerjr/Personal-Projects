
N = 1000
prime_sieve = [1 for i in range(0,N)]
sieve = [1 for i in range(0,N)]

def primeSieve():
    for i in range(2,N):
        for j in range(i+i,N,i):
            prime_sieve[j] = 0
    
def modifiedSieve():
    for i in range(2,N):
        if i not in (3,5,7) and prime_sieve[i] == 1:
            for j in range(i,N,i):
                sieve[j] = 0
        
        
def kth(K):
    k = 0
    i = 3
    while k < K and i < N:
        if sieve[i]:
            k += 1
            
        i += 1

    return i-1

primeSieve()
modifiedSieve()

print(kth(4))
print(kth(5))
print(kth(6))
