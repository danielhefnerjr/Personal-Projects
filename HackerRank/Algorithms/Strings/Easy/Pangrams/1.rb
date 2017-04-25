# Enter your code here. Read input from STDIN. Print output to STDOUT

s = gets.strip.downcase
puts ('a'..'z').all? { |i| s.include? i } ? 'pangram' : 'not pangram'