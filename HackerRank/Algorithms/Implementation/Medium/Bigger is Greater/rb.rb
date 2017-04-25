# Enter your code here. Read input from STDIN. Print output to STDOUT

def next_permutation(a)
    i = a.length - 1
    while i > 0 && a[i-1] >= a[i]
        i -= 1
    end
    
    if i <= 0 
        return nil
    end
    
    j = a.length - 1
    while a[j] <= a[i-1]
        j -= 1
    end
    
    a[i-1], a[j] = a[j], a[i-1]
    
    a[i..-1] = a[i..-1].reverse
    
    a
end

t = gets.strip.to_i
t.times {
    w = gets.strip
    
    p = next_permutation(w.split(''))
    puts p ? p.join : 'no answer'
}