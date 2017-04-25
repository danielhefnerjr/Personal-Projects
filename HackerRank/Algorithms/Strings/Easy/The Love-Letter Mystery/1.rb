# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i
t.times do
    s = gets.strip.split('')
    puts (0..s.size/2-1).map { |i| (s[i].ord - s[-1-i].ord).abs }.inject :+
end