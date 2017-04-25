# INCORRECT 
# count nodes in subtree, if it has even nodes, cut
# alternatively, count edges in subtree, if odd edges, cut

# how to efficiently count nodes/edges in all subtrees?

# count nodes with even degree?
m,n = gets.strip.split.map &:to_i
edges = Hash.new { |h,k| h[k] = [] }
n.times do
    v1,v2 = gets.strip.split.map &:to_i
    edges[v1] << v2
    edges[v2] << v1
end

puts edges.count { |v,e| edges[v].size.even? }