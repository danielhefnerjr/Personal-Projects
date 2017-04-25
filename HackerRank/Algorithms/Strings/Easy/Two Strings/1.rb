# Enter your code here. Read input from STDIN. Print output to STDOUT
require('set')
p = gets.strip.to_i

p.times do
    a = gets.strip.split('').to_set
    b = gets.strip.split('').to_set
    puts a.intersect?(b) ? 'YES' : 'NO'
end