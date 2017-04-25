# Enter your code here. Read input from STDIN. Print output to STDOUT
n = gets.strip.to_i
d = gets.strip.split(' ').map &:to_i

if d.sort == d
    puts 'yes'
else
    diff = []
    d.sort.each_with_index do |x,i|
        if d[i] != x
            diff << i
        end
    end
    if diff.size == 2
        puts "yes\nswap #{diff[0]+1} #{diff[1]+1}"
    else
        pre = d[0..diff[0]-1]
        post = d[diff[-1]+1..d.length]
        flip = d[diff[0]..diff[-1]]
        if d.sort == pre + flip.reverse + post
            puts "yes\nreverse #{diff[0]+1} #{diff[-1]+1}"
        else
            puts 'no'
        end
    end
    
end