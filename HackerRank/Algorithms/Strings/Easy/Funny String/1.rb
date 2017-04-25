# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i
t.times do
    s = gets.strip
    r = s.reverse
    puts (1..s.size-1).all? { |i| (s[i].ord-s[i-1].ord).abs == (r[i].ord-r[i-1].ord).abs } ? 'Funny' : 'Not Funny'
end