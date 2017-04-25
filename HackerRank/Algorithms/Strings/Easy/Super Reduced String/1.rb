# Enter your code here. Read input from STDIN. Print output to STDOUT
s = gets.strip
rep = true

while rep
    new = s.gsub(/(.)\1/,'')
    rep = new != s
    s = new
end

puts s.length == 0 ? 'Empty String' : s
