#!/bin/ruby

n,t = gets.strip.split(' ')
n = n.to_i
t = t.to_i
width = gets.strip
width = width.split(' ').map(&:to_i)
for a0 in (0..t-1)
    i,j = gets.strip.split(' ')
    i = i.to_i
    j = j.to_i
    
    puts width[i..j].min
end
