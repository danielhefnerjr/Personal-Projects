# failed: just realized, tree is not necessarily binary (duh!)
# solution: build adjacency lists from edges, choose first node with < 3 children as root, construct tree from there
#           depth first search to find min, comparing cutting left and right subtrees of current node with dfs of both children
# complexity: O(V + E) for search, O(V + E) to build (loop through each adjacency list of each node)
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

def buildTree(edges)
    r = edges.select {|key,children| children.size < 3}.first[0]
    t = Tree.new(r)
    inserted = [false]*edges.size
    inserted[r-1] = true
    
    q = [t]
    until q.empty? do
        r = q.shift
        children = edges[r.val]
        for child in children
            if !inserted[child-1]
                if !r.left
                    r.left = Tree.new(child)
                    q.push r.left
                else
                    r.right = Tree.new(child)
                    q.push r.right
                end
                inserted[child-1] = true
            end
        end
    end
    
    return t
end
n = gets.strip.to_i
@vv = gets.strip.split.map &:to_i
edges = Hash.new([])
(n-1).times do
    v1,v2 = gets.strip.split.map &:to_i 
    edges[v1] += [v2]
    edges[v2] += [v1]
end



#edges.each {|parent,children| children.each { |child| insertAt(t,child,parent) if !inserted[child-1] }}

t= buildTree(edges)
puts findMin(t,sumVals(t))