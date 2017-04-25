# Enter your code here. Read input from STDIN. Print output to STDOUT
n = gets.strip.to_i
d = gets.strip.split(' ').map &:to_i

if d.each_cons(2).all?{|i,j| i <= j}
    puts 'yes'
    exit
end

if d.length == 2
	puts 'yes'
	puts 'swap 1 2'
	exit
end

swaps = d.each_index.select { |i| i == 0 ? d[0] > d[1] : d[i] < d[i-1] }


if swaps.length > 2
	d = d[0..swaps[0]-2] + d[swaps[0]-1..swaps[-1]].reverse + d[swaps[-1]+1..n]
	if d.each_cons(2).all?{|i,j| i <= j}
	    puts 'yes'
	    puts 'reverse ' + (swaps[0]).to_s + ' ' + (swaps[-1]+1).to_s
	    exit
	end
end

if swaps.length == 1
	d[swaps[0]-1], d[swaps[0]] = d[swaps[0]], d[swaps[0]-1]
	
	if d.each_cons(2).all?{|i,j| i <= j}
	    puts 'yes'
	    puts 'swap ' + (swaps[0]).to_s + ' ' + (swaps[0]+1).to_s
	    exit
    else
    	puts 'no'
    	exit
	end
end

d[swaps[0]-1], d[swaps[1]] = d[swaps[1]], d[swaps[0]-1]
if d.each_cons(2).all?{|i,j| i <= j}
    puts 'yes'
    puts 'swap ' + (swaps[0]).to_s + ' ' + (swaps[1]+1).to_s
    exit
end

#d[swaps[0]], d[swaps[1]] = d[swaps[1]], d[swaps[0]]

puts 'no'