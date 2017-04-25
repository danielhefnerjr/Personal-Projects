# Enter your code here. Read input from STDIN. Print output to STDOUT
a = gets.strip
b = gets.strip
counts_a = a.scan(/\w/).inject(Hash.new(0)){|h,c| h[c] += 1; h } 
counts_b = b.scan(/\w/).inject(Hash.new(0)){|h,c| h[c] += 1; h }
puts ('a'..'z').map { |c| (counts_a[c] - counts_b[c]).abs }.inject(:+)