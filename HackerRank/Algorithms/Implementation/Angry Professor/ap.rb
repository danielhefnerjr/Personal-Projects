#!/bin/ruby

t = gets.strip.to_i
for a0 in (0..t-1)
    n,k = gets.strip.split(' ')
    n = n.to_i
    k = k.to_i
    a = gets.strip
    a = a.split(' ').map(&:to_i)
    
    puts (a.map {|i| (i <= 0) ? 1 : 0} .reduce(:+) >= k ) ? 'NO' : 'YES'
end
