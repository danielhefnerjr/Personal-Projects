#SUCCESSFUL
#faster -- removes dfs for subtrees with odd number of edges, instead keeping count as it finds them
# O(V+E)
m,n = gets.strip.split.map &:to_i
@edges =Hash.new {|h,k| h[k] = [] }
n.times do
	v1,v2 = gets.strip.split.map &:to_i
	@edges[v1].push v2
	@edges[v2].push v1
end
@count = 0
def countSubtreeEdges(v, edges) 
	if edges.size == 0
		return 0	
	end
	ret = edges.size + edges.map{ |u| countSubtreeEdges(u, @edges[u] - [v]) }.inject(:+)
	@count += 1 if ret.odd?
	return ret
	
end

countSubtreeEdges(1,@edges[1])
puts @count - 1