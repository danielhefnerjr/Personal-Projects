# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i
for i in 1..t
    a,b = gets.strip.split(' ').map &:to_i
    
    
    puts (Math.sqrt(a).ceil..Math.sqrt(b).floor).count
end