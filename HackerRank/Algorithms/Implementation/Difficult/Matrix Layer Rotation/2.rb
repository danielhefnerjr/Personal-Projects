
# Enter your code here. Read input from STDIN. Print output to STDOUT
@m,@n,@r = gets.strip.split.map &:to_i

@a = []
@m.times { |i|
    @a << (gets.strip.split.map &:to_i)
}

def rotate(layer)
    n = @n - 2*layer
    m = @m - 2*layer
    
    #puts layer, m,n
    unraveled_layer = []
    
    #top
    unraveled_layer += @a[layer][layer,n].reverse
    
    #left
    for i in layer+1..layer + m-2 #@m-1-layer-1
        unraveled_layer << @a[i][layer] 
    end
    
    #bottom
    unraveled_layer += @a[-1-layer][layer,n]
    
    #right
    for i in (layer+1..layer + m - 2).reverse_each #n-1-layer-1).reverse_each
        unraveled_layer << @a[i][-1-layer]
    end
    
    #puts unraveled_layer.join (' ')
    
    rotated_layer = []
    for i in 0..unraveled_layer.length - 1
        rotated_layer << unraveled_layer[(i-@r) % unraveled_layer.length] 
    end
	
    #puts rotated_layer.join ' '
    
    #top
    @a[layer][layer,n] = rotated_layer[0,n].reverse
    
    #left    
    for i,x in (layer+1..@m-1-layer-1).zip((n..n+m-2))
        @a[i][layer] = rotated_layer[x]
    end
    
    #bottom
    @a[-1-layer][layer,n] = rotated_layer[n+m-2,n]
    
    #right
    for i,x in (layer+1..@m-1-layer-1).reverse_each.zip((n+m-2+n..n+n+m-2+m-2-1))
        @a[i][-1-layer] = rotated_layer[x]
    end
    
    
end

#rotate(1)
(0..([@m,@n].min/2) - 1).each { |l| 
    rotate(l)
    }

@a.each {|r| puts r.join(' ') }