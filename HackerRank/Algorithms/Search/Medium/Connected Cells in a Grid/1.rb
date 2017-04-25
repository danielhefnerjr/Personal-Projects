# Enter your code here. Read input from STDIN. Print output to STDOUT
def searchRegion(i,j,c)
    if @a[i][j] == 0 || @a[i][j] == 'X'
        return c
    end
    c += 1
    @a[i][j] = 'X'
    for d_i in -1..1
        for d_j in -1..1
            if (d_i + i) >= 0 && (d_i + i) < @a.size && (d_j + j) >= 0 && (d_j + j) < @a[0].size
                c = searchRegion(d_i+i,d_j+j,c)
            end
        end
    end
    
    return c
end

n = gets.strip.to_i
m = gets.strip.to_i
@a = []
n.times do
    @a << gets.strip.split.map(&:to_i)
end
r = []
for i in 0...n
    for j in 0...n
        if @a[i][j] == 1
            r << searchRegion(i,j,0)
        end
    end
end
puts r.max
