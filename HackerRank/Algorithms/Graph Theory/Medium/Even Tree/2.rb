# CORRECT
# but slow
# complexity: O((V+E)^2) ?
m,n = gets.strip.split.map &:to_i
@edges =Hash.new {|h,k| h[k] = [] }
n.times do
	v1,v2 = gets.strip.split.map &:to_i
	@edges[v1].push v2
	@edges[v2].push v1
end

def countSubtreeEdges(v, edges) 
	if edges.size == 0
		return 0	
	end
	
	return edges.size + edges.map{ |u| countSubtreeEdges(u, @edges[u] - [v]) }.inject(:+)
	
end

def countOddEdgeSubtrees(v, edges)
	if edges.size < 1
		return 0
	end
	
	evensubs = edges.map {|u| countOddEdgeSubtrees(u, @edges[u]-[v])}.inject(:+)
	subedges = countSubtreeEdges(v,edges)
	#puts v.to_s + ': ' + evensubs.to_s + ' ' + subedges.to_s
	return evensubs + (subedges.odd? ? 1 : 0)
end

puts countOddEdgeSubtrees(1,@edges[1])-1