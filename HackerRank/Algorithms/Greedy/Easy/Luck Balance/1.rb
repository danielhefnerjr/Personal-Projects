# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = gets.strip.split.map &:to_i
important = []
unimportant = []
n.times do
    l,t = gets.strip.split.map &:to_i
    if t == 1
        important << l 
    else
        unimportant << l
    end
end

important.sort!.reverse!
luck = 0
if !important.empty? && k > 0
    luck += important[0...k].inject(:+)
end
if important.length > k
	luck -= important[k...n].inject(:+)
end
if !unimportant.empty?
    luck += unimportant.inject(:+)
end
puts luck
