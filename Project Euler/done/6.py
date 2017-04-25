#.............Problem 6...................
N = 100
s = N*(N+1)/2
sq_of_sum = s**2
sum_of_sq = sum([x**2 for x in range(1,N+1)])
diff = abs(sum_of_sq - sq_of_sum)
print(diff)
