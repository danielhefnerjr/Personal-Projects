#!/bin/ruby

n = gets.strip.to_i
#f = 1
#for i in (2..n)
#    f *= i
#end

#puts f
puts (1..n).inject :*