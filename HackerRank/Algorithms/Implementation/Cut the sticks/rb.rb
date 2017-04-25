#!/bin/ruby

n = gets.strip.to_i
arr = gets.strip
arr = arr.split(' ').map(&:to_i)

while arr.any? { |x| x > 0}
    c = arr.length
    m = arr.min
    arr = arr.map {|x| x - m}.select {|x| x > 0}
    puts c
end