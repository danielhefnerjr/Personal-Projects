# Enter your code here. Read input from STDIN. Print output to STDOUT
n,d = gets.strip.split.map &:to_i
a = gets.strip.split.map &:to_i

c = 0
a.each {|x|
    # could speed up lookup by putting each element in hash
    if a.include?(x+d) && a.include?(x+2*d)
        c += 1
    end
}

puts c