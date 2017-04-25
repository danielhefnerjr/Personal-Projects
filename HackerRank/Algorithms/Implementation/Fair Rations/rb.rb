#!/bin/ruby

n = gets.strip.to_i
b = gets.strip
b = b.split(' ').map(&:to_i)

if b.length <= 1 || b.count(&:odd?).odd?
    puts 'NO'
else
    c = 0
    while b.any?(&:odd?)
        i = b.each_index.select {|i| b[i].odd?}.first
        b[i] += 1
        b[i+1] += 1
        c += 2
    end
    
    puts c
end