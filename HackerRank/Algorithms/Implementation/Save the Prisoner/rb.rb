# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i

for i in 1..t
    n,m,s = gets.strip.split(' ').map &:to_i
    p = (s+m -1)%n
   puts p == 0 ? n : p
end