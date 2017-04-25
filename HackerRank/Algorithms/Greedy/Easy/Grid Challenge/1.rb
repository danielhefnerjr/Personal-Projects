# Enter your code here. Read input from STDIN. Print output to STDOUT

t = gets.strip.to_i
t.times do 
    n = gets.strip.to_i
    m = []
    n.times do 
        m << gets.strip.split('').sort
    end
    
    sorted = true
    n.times do |j|
        (n-1).times do |i|
             if m[i+1][j] < m[i][j]
                 sorted = false
             end
        end
    end
    
    puts sorted ? 'YES' : 'NO'
end
