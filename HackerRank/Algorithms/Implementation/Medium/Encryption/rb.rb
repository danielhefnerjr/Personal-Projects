#!/bin/ruby

s = gets.strip.gsub(/\s+/,'')

n = (s.length ** 0.5).ceil
l= s.split('').each_slice(n).to_a
m = l[0].zip(*l[1..-1])
puts m.map { |x| x.join }.join ' '