# Enter your code here. Read input from STDIN. Print output to STDOUT
n = gets.strip.to_i
s = gets.strip
diffs = s.scan(/[GACT]/).inject(Hash.new(n/4)) { |h,c| h[c] -= 1; h }
over = diffs.select { |k,v| v < 0 }.map { |k,v| [k, v * -1] }.to_h
#over.default = 0
if over.size == 0
    puts 0
    exit
end

found = Hash.new(0)
min = Float::INFINITY
i = 0
j = 0
while i < s.size && j < s.size
    while over.any? {|k,v| found[k] < v}
        found[s[j]] += 1
        j += 1
    end
    while over.all? {|k,v| found[k] > v}
        found[s[i]] -= 1
        i += 1
    end
    min = [j-i,min].min
    found[s[i]] -= 1
    i += 1
end
puts min