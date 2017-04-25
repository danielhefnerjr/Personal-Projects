# Enter your code here. Read input from STDIN. Print output to STDOUT

s = gets.chomp 

h = s.scan(/\w/).inject(Hash.new(0)) { |h,c| h[c] += 1; h }
odds = h.select { |k,v| v.odd? }
puts (s.size.even? && odds.size == 0) || (s.size.odd? && odds.size == 1) ? 'YES' : 'NO'