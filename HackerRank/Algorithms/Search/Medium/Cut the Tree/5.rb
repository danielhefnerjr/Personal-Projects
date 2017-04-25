# failed: tried to speed up by memoizing sums at each node, get stack level too deep on recursion
# solution: build adjacency lists from edges, choose first node with < 3 children as root, construct tree from there
#           depth first search to find min, comparing cutting left and right subtrees of current node with dfs of both children
# complexity: O(V + E) for search, O(V) to build (loop through each adjacency list of each node), O(V + E) to memoize sums (dfs)
Tree = Struct.new(:val, :children)


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
	return 0 if !t
	
	s = @vv[t.val-1]
	
    for child in t.children
        s += sumVals(child) 
    end
    @sums[t.val-1] = s
	return s
end

def isIn(t,v)
	return false if !t
	if t.val == v
		return true
	else
		return false if !t.children
		
        flag = false
        for child in t.children
            flag ||= isIn(child,v)
        end
        return flag 
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
                r.children.push Tree.new(child, [])
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