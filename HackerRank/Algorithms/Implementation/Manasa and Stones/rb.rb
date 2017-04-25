# Enter your code here. Read input from STDIN. Print output to STDOUT

#def find_end_values(i,n,a,b,x)
#    if i == n
#        $end_values << x
#    else
#        find_end_values(i+1,n,a,b,x+a)
#        find_end_values(i+1,n,a,b,x+b)
#    end
#end

$end_values = []
t = gets.strip.to_i

for _ in 1..t
    n = gets.strip.to_i
    a = gets.strip.to_i
    b = gets.strip.to_i
    
    #find_end_values(1,n,a,b,0)
    
    #for i in 0..2**(n-1)-1
    #    $end_values << ('%0*b' % [n-1,i]).split('').map {|x| x == '0' ? a : b}.inject(:+)
    #end
    for i in 0..n-1
        $end_values << a*(n-1-i)  + b*i
    end
    puts $end_values.uniq.sort.join(' ')
    $end_values = []
end