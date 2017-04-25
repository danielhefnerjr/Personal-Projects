# Enter your code here. Read input from STDIN. Print output to STDOUT

n = gets.strip.to_i
a = gets.strip.split.map &:to_i
m = gets.strip.to_i
b = gets.strip.split.map &:to_i

counts_a = a.inject(Hash.new(0)) { |h,x| h[x] += 1; h }
counts_b = b.inject(Hash.new(0)) { |h,x| h[x] += 1; h }

missing = a.select { |x| counts_a[x] != counts_b[x] } | b.select { |x| counts_a[x] != counts_b[x] }
missing.sort!

puts missing.join(' ')