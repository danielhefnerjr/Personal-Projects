# Enter your code here. Read input from STDIN. Print output to STDOUT
n = gets.strip.to_i
s = gets.strip
diffs = s.scan(/[GACT]/).inject(Hash.new(n/4)) { |h,c| h[c] -= 1; h }
over = diffs.select { |k,v| v < 0 }.map { |k,v| [k, v * -1] }.to_h
over.default = 0
if over.size == 0
    puts 0
    exit
end

found = Hash.new(0)
min = Float::INFINITY
i = 0
j = 0
count = 0
# http://articles.leetcode.com/finding-minimum-window-in-s-which/
for j in 0...s.size
    next if over[s[j]] == 0
    found[s[j]] += 1
    count += 1 if found[s[j]] <= over[s[j]]
        
    if count == over.values.inject(:+)
        while over[s[i]] == 0 || found[s[i]] > over[s[i]]
            if found[s[i]] > over[s[i]]
                found[s[i]] -= 1
            end
            i += 1
        end
        min = [j-i+1,min].min
    end
end
puts min