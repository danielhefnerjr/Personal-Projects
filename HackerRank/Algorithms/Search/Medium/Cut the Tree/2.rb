# failed: too slow and not all nodes get input in tree
# solution: build adjacency lists from edges, choose first node with < 3 children as root, construct tree from there
#           depth first search to find min, comparing cutting left and right subtrees of current node with dfs of both children
# complexity: O(V + E) for search, O(V^3 + E) to build (loop through each adjacency list of each node, run dfs and insert on each)
Tree = Struct.new(:val, :left, :right)


def findMin(t,total)
	return Float::INFINITY if !t || (!t.left && !t.right)
	#total += @vv[t.val-1]
	m = [(total - 2*sumVals(t.right)).abs, (total - 2*sumVals(t.left)).abs,
		findMin(t.left,total),findMin(t.right,total)].min
	#puts t,m
	m
end

def sumVals(t)
	return 0 if !t
	return @vv[t.val-1] + sumVals(t.left) + sumVals(t.right)
end

def insertAt(t,v,r)
	return false if !t
	if !r
		t.val = v
		return true
	else
		if t.val == r
			if !t.left
				t.left = Tree.new(v)
			else
				t.right = Tree.new(v)
			end
		else
			return insertAt(t.left,v,r) || insertAt(t.right,v,r)
		end
	end
end

def isIn(t,v)
	return false if !t
	if t.val == v
		return true
	else
		return isIn(t.left,v) || isIn(t.right,v)
	end
end

n = gets.strip.to_i
@vv = gets.strip.split.map &:to_i
edges = Hash.new([])
(n-1).times do
    v1,v2 = gets.strip.split.map &:to_i 
    edges[v1] += [v2]
    edges[v2] += [v1]
end


r = edges.select {|key,children| children.size < 3}.first[0]
t = Tree.new
insertAt(t,r,nil)
edges.each {|parent,children| children.each { |child| insertAt(t,child,parent) if !isIn(t,child) }}
puts findMin(t,sumVals(t))