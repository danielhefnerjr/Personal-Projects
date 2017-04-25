# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = gets.strip.split(' ').map &:to_i
a = gets.strip.split(' ').map(&:to_i).map {|x| x % k}

equiv_classes = Hash.new(0)
a.each {|x| equiv_classes[x] += 1}

c = 0
if k.odd?
    for i in 1..k/2
        c += [equiv_classes[i],equiv_classes[k-i]].max
    end
    c += 1 if equiv_classes[0] > 0
else
    for i in 1..k/2-1
        c += [equiv_classes[i],equiv_classes[k-i]].max 
    end
    
    c += 1 if equiv_classes[0] > 0
    c += 1 if equiv_classes[k/2] > 0
end

puts c