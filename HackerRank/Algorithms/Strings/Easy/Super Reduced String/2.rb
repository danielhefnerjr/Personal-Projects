# Enter your code here. Read input from STDIN. Print output to STDOUT
s = gets.strip

100.times { s = s.gsub(/(.)\1/,'') }

puts s.empty? ? 'Empty String' : s
