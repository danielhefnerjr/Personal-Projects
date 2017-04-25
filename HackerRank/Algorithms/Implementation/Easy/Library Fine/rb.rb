#!/bin/ruby

d1,m1,y1 = gets.strip.split(' ')
d1 = d1.to_i
m1 = m1.to_i
y1 = y1.to_i
d2,m2,y2 = gets.strip.split(' ')
d2 = d2.to_i
m2 = m2.to_i
y2 = y2.to_i

if y1 < y2
    fine = 0
elsif y1 == y2
    if m1 < m2
        fine = 0
    elsif m1 == m2
        if d1 <= d2
            fine = 0
        else
            fine = 15 * (d1-d2) 
        end
    else
        fine = 500 * (m1-m2)
    end
else
    fine = 10000
end

puts fine