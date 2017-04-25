#!/bin/ruby

n = gets.strip.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)

if n == 1
    puts -1
else
    m = a.each.with_index.sort_by(&:first).each_cons(2).map {|((x,i),(y,j))| x==y && i != j ? (i-j).abs : Float::INFINITY}.min
    puts m == Float::INFINITY ? -1 : m
end
