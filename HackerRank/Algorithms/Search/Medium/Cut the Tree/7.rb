# SUCCESSFUL
# solution: Post Order DFS through tree using a stack.  When visiting a node, sum all children and itself and split on it,
#           calculating tree_diff as abs(total - 2 * current_node_sum).  Keep track of minimum tree_diff.
# complexity: O(V + E) for dfs

def dfs(edges, values)
	m = Float::INFINITY
    total = values.inject :+
    
	sums = [0] * n
	
    seen = [false] * edges.size
    seen[0] = true
    stack = [1]
    
    until stack.empty?
    	curr = stack[-1]
    	children = edges[curr].select { |i| seen[i-1] == false }
    	
    	# if no unvisited children, visit
    	if children.empty?
    		stack.pop()
            # no need to filter out parent node's sum as it is still 0 until visited (after current node)
    		sums[curr-1] = values[curr-1] + (edges[curr].map {|v| sums[v-1]}.inject :+)
    		m = [m,(total - 2* sums[curr-1]).abs].min
    	end
    	children.each { |c| seen[c-1] = true; stack.push c }
    end
    
    puts m
end


n = gets.strip.to_i
vv = gets.strip.split.map &:to_i
edges = Hash.new([])
(n-1).times do
    v1,v2 = gets.strip.split.map &:to_i 
    edges[v1] += [v2]
    edges[v2] += [v1]
end
puts dfs(edges,vv)