# Enter your code here. Read input from STDIN. Print output to STDOUT
def search(i,j,waves,visited)
    #puts visited.join(' ')
    if @a[i][j] == '*'
        return waves
    end
    if @a[i][j] == 'X'
        return -1
    end
    
    ways = 0
    ways += 1 if i > 0 && @a[i-1][j] != 'X' && !visited.include?([i-1,j])
    ways += 1 if i+1 < @a.size && @a[i+1][j] != 'X' && !visited.include?([i+1,j])
    ways += 1 if j > 0 && @a[i][j-1] != 'X' && !visited.include?([i,j-1])
    ways += 1 if j+1 < @a[0].size && @a[i][j+1] != 'X' && !visited.include?([i,j+1])
    #puts "#{i} #{j} #{ways} #{waves}"
    waves += 1 if ways > 1
    
    t = []
    #up
    if i > 0 && !visited.include?([i-1,j])
        t << search(i-1,j,waves,visited + [[i-1,j]])
    end
    
    #down
    if i+1 < @a.size && !visited.include?([i+1,j])
        t << search(i+1,j,waves, visited + [[i+1,j]]) 
    end
    
    #left
    if j > 0 && !visited.include?([i,j-1])
        t << search(i,j-1,waves,visited + [[i,j-1]])
    end
    
    #right
    if j+1 < @a[0].size && !visited.include?([i,j+1])
        t << search(i,j+1,waves,visited + [[i,j+1]])
    end
    
    
    return t.max
end 

t = gets.strip.to_i

t.times do
    n,m = gets.strip.split.map &:to_i
    @a = []
    si, sj = 0, 0
    n.times do |i|
        @a << gets.strip.split('')
        if @a[i].include? 'M'
            si = i
            sj = @a[i].index('M')
        end
    end
    
    k = gets.strip.to_i
    #puts search(si,sj,0,[[si,sj]])
    puts search(si,sj,0,[[si,sj]]) == k ? 'Impressed' : 'Oops!'
    
end