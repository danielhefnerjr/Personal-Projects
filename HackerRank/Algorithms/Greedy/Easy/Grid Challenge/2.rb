# Enter your code here. Read input from STDIN. Print output to STDOUT

t = gets.strip.to_i
t.times do 
    n = gets.strip.to_i
    m = n.times.map do 
        gets.strip.split('').sort
    end
    
    puts m.transpose.all? { |s| s == s.sort } ? 'YES' : 'NO'
end
