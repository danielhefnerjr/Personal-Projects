#!/bin/ruby

t = gets.strip.to_i

s = 1
n = 0

while s <= t
    s += 3 * 2**n
    n += 1
end
n -= 1
s -= 3 * 2**n
#puts s
c = (3*2**n)-(t-s)
puts c
