# Enter your code here. Read input from STDIN. Print output to STDOUT
n = gets.strip.to_i
rocks = n.times.map { gets.strip }
puts ('a'..'z').map { |a| rocks.all? { |r| r.include? a } }.count true