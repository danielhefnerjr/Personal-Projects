#!/bin/ruby

s = gets.strip
n = gets.strip.to_i

times = n/s.size
puts times * s.count('a') + s[0...n-times*s.size].count('a')