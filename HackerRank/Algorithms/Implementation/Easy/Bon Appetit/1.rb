# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = gets.strip.split.map &:to_i
c = gets.strip.split.map &:to_i
b = gets.strip.to_i

s = c.inject(:+) - c[k]
if s/2 == b
    puts 'Bon Appetit'
else
    puts b - s/2
end