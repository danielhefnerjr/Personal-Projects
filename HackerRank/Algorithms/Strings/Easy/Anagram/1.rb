# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i
t.times do
    s = gets.strip.split('')
    a = s[0,s.size/2]
    b = s[s.size/2..-1]
    
    if a.size != b.size
        puts -1
        next
    end
    
    counts_a = Hash.new(0)
    counts_b = Hash.new(0)
    a.each { |x| counts_a[x] += 1 }
    b.each { |x| counts_b[x] += 1 }
    
    puts ('a'..'z').map { |x| (counts_b[x]-counts_a[x]).abs }.inject(:+) / 2
    
end