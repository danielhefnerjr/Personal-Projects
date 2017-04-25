# Enter your code here. Read input from STDIN. Print output to STDOUT

p = gets.strip.to_i
q = gets.strip.to_i

def isKaprekar(n)
    d = n.to_s.length
	# s = n*n
	# l = s.to_s[0..-d-1]
	# r = s.to_s[-d..-1]
	
    s = (n*n).to_s.reverse
    r = s[0,d].reverse
    l = s[d,d].reverse
    
    l.to_i + r.to_i == n
end
c = 0
l = []
(p..q).each {|n| 
    if isKaprekar(n)
        l << n
        c += 1
    end}

puts (c > 0 ? l.join(' ') : 'INVALID RANGE')