# Enter your code here. Read input from STDIN. Print output to STDOUT
require('set')
p = gets.strip.to_i

p.times do
    a = gets.strip.split('')
    b = gets.strip.split('')
    puts a & b != [] ? 'YES' : 'NO'
end