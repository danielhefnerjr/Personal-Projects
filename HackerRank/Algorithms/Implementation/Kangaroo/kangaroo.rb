#!/bin/ruby

x1,v1,x2,v2 = gets.strip.split(' ')
x1 = x1.to_i
v1 = v1.to_i
x2 = x2.to_i
v2 = v2.to_i

if v1 == v2
    if x1 == x2
        puts 'YES'
    else
        puts 'NO'
    end
else   
    t = (x1-x2)/(v2-v1).to_f
    puts((t % 1 == 0 && t > 0) ? 'YES' : 'NO')
end
        