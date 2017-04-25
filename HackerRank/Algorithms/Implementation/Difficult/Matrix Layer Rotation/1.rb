
# Enter your code here. Read input from STDIN. Print output to STDOUT
@m,@n,r = gets.strip.split.map &:to_i

@a = []
@m.times { |i|
    @a << (gets.strip.split.map &:to_i)
}

def rotate(layer)
	# top: i = layer, j = layer..n-1-layer-1
    xt = @a[layer][layer]
    for j in layer..@n-1-layer-1
        @a[layer][j] = @a[layer][j+1] 
    end
    
    # left: j = layer, i = layer+1..m-1-layer
    xl = @a[-1-layer][layer]
    
    for i in (layer+1..@m-1-layer).reverse_each
        @a[i][layer] = @a[i-1][layer] 
    end
    
    @a[layer+1][layer] = xt
    
    # bottom: i = -1-layer, j = layer..n-1-layer
    xb = @a[-1-layer][-1-layer]
    
    for j in (layer+2..@n-1-layer).reverse_each
        @a[-1-layer][j] = @a[-1-layer][j-1]
    end
    
    @a[-1-layer][layer+1] = xl
    
    # right: j = -1-layer, i = layer..m-1-layer
    for i in layer..@m-1-layer-1
        @a[i][-1-layer] = @a[i+1][-1-layer]
    end	
    
    @a[-1-layer-1][-1-layer] = xb
	
end

r.times {
	(0..([@m,@n].min/2) - 1).each { |l| 
		rotate(l)
	}
}

@a.each {|r| puts r.join(' ') }