#!/bin/ruby

n,k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
c = gets.strip
c = c.split(' ').map(&:to_i)

e = 100
i = 0
begin
    i = (i+k) % n
    e -= c[i] == 1 ? 3 : 1
end while e > 0 && i != 0

puts e