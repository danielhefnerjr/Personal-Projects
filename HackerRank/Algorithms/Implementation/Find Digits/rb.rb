#!/bin/ruby

t = gets.strip.to_i
for a0 in (0..t-1)
    n = gets.strip.to_i
    c = 0
    n.to_s.split('').map {|d| c+= 1 if d.to_i != 0 && n % d.to_i == 0 }
    puts c
end
