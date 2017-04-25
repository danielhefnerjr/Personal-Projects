#!/bin/ruby

t = gets.strip.to_i
for a0 in (0..t-1)
    n,c,m = gets.strip.split(' ')
    n = n.to_i
    c = c.to_i
    m = m.to_i
    
    chocolates = n/c
    wrappers = chocolates
    while wrappers >= m
        chocolates += wrappers/m
        wrappers = wrappers % m + wrappers/m
    end
    
    puts chocolates
end
