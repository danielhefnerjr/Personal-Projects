#!/bin/ruby

n = gets.strip.to_i
b = gets.strip

b2 = b.gsub(/010/,'011')
puts (b.count('1')-b2.count('1')).abs
