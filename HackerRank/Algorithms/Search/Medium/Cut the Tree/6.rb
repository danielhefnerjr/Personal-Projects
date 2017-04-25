# failed: made sum memoization bfs with q and traversing parents to update their sums, still slightly too slow
# solution: build adjacency lists from edges, choose first node with < 3 children as root, construct tree from there
#           depth first search to find min, comparing cutting left and right subtrees of current node with dfs of both children
# complexity: O(V + E) for search, O(V + E) to build (loop through each adjacency list of each node), O(V + E + logn) to memoize sums (dfs +
#             traversal of parents)
Tree = Struct.new(:val, :children, :parent)


def findMin(t,total)
	return Float::INFINITY if !t || !t.children
	#total += @vv[t.val-1]
	q = [t]
	m = Float::INFINITY
	until q.empty?
		r = q.shift
		#next if !r.children
		for child in r.children
            m = [(total - 2*@sums[child.val-1]).abs,m].min
			q.push child
		end
	end
	#puts t,m
	m
end

def sumVals(t)
	return if !t
	
	@sums[t.val-1] = @vv[t.val-1]
	q = [t]
	until q.empty? do
		r = q.shift
		@sums[r.val-1] += @vv[r.val-1] # = or += ?
	    for child in r.children
	        q.push child
	    end
	    
	    p = r.parent
	    while p
	    	@sums[p.val-1] += @vv[r.val-1]
	    	p = p.parent
	    end
    end
end

def buildTree(edges)
    r = edges.select {|key,children| children.size < 3}.first[0]
    t = Tree.new(r, [])
    inserted = [false]*edges.size
    inserted[r-1] = true
    
    q = [t]
    until q.empty? do
        r = q.shift
        children = edges[r.val]
        for child in children
            if !inserted[child-1]
            	#r.children = [] if !r.children
                r.children.push Tree.new(child, [], r)
                q.push r.children[-1]
                inserted[child-1] = true
            end
        end
    end
    
    return t
end
n = gets.strip.to_i
@vv = gets.strip.split.map &:to_i
@sums = [0] * n
edges = Hash.new([])
(n-1).times do
    v1,v2 = gets.strip.split.map &:to_i 
    edges[v1] += [v2]
    edges[v2] += [v1]
end
t = buildTree(edges)
sumVals(t)
puts findMin(t,@vv.inject(:+))