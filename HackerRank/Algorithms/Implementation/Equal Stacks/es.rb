#!/bin/ruby

n1,n2,n3 = gets.strip.split(' ')
n1 = n1.to_i
n2 = n2.to_i
n3 = n3.to_i
h1 = gets.strip
h1 = h1.split(' ').map(&:to_i)
h2 = gets.strip
h2 = h2.split(' ').map(&:to_i)
h3 = gets.strip
h3 = h3.split(' ').map(&:to_i)
H1 = h1.reduce :+
H2 = h2.reduce :+
H3 = h3.reduce :+
while H1 != H2 || H2 != H3 do
    while H1 > H2 || H1 > H3 do
        h = h1.shift
        H1 -= h
    end
    
    while H2 > H1 || H2 > H3 do
        h = h2.shift
        H2 -= h
    end
    
    while H3 > H1 || H3 > H2 do
        h = h3.shift
        H3 -= h
    end
end

puts H1