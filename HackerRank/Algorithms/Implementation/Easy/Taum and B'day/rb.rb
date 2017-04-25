#!/bin/ruby

t = gets.strip.to_i
for a0 in (0..t-1)
    b,w = gets.strip.split(' ')
    b = b.to_i
    w = w.to_i
    x,y,z = gets.strip.split(' ')
    x = x.to_i
    y = y.to_i
    z = z.to_i
    
    x = [x,y+z].min
    y = [y,x+z].min
    
    puts x*b + y*w
    
end
