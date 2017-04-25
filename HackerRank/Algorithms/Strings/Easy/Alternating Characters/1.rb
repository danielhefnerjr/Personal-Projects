# Enter your code here. Read input from STDIN. Print output to STDOUT

n = gets.strip.to_i
n.times do 
    s = gets.strip
    puts (s.size - s.gsub(/(.)\1+/,'\1').size).abs
end