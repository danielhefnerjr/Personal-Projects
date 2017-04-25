# Enter your code here. Read input from STDIN. Print output to STDOUT
t = gets.strip.to_i
t.times do
    m = gets.strip.to_i
    n = gets.strip.to_i
    c_ar = gets.strip.split.map &:to_i
    
    h = m/2.0
    if c_ar.count(h) > 1
        puts (c_ar.index(h)+1).to_s + ' ' + (c_ar.rindex(h)+1).to_s
        next
    end
    
    
    indices = {}
    c_ar.each.with_index { |c,i| indices[c] = i }
    c_ar.each.with_index do |c,i|
        if  c != m - c && indices.include?(m-c)
            puts (i+1).to_s + ' ' + (indices[m-c]+1).to_s
            break
        end
    end
        
end