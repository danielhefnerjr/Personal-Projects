# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i

t.times do
    n = gets.strip.to_i
    a = gets.strip.split.map &:to_i
    
    if a.size == 1 || a[1..-1].inject(:+) == 0
        puts 'YES'
        next
    end
    
    sum_l = 0
    sum_r = a[1..-1].inject :+
    i = 1
    while i < a.size && sum_l != sum_r
        sum_l += a[i-1]
        sum_r -= a[i]
        i += 1
    end
    
    puts i < a.size ? 'YES' : 'NO'
end