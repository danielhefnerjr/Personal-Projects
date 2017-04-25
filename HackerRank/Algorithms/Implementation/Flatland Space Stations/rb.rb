#!/bin/ruby

n,m = gets.strip.split(' ')
n = n.to_i
m = m.to_i
cs = gets.strip
cs = cs.split(' ').map(&:to_i).sort

dists = [0] * n
for i in 0..cs[0]
    dists[i] = cs[0] - i 
end

for i in cs[-1]..n-1
    dists[i] = i - cs[-1] 
end

cs.each_cons(2) do |(c1,c2)|
	puts c1,c2
    mid = c1 + (c2-c1)/2
    
    for i in c1..mid
        dists[i] = i-c1 
    end
    #dists[mid] = [mid-c1,c2-mid].min
    for i in mid+1..c2
        dists[i] = c2-i 
    end
end
#puts dists.join(' ')
puts dists.max