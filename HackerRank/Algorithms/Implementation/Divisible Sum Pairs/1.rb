#!/bin/ruby

n,k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)

count = 0
for j in 0..n-1 do
    for i in 0..j-1 do
        if (a[i] + a[j]) % k ==0
            count += 1
        end
    end
end

puts count
    
   