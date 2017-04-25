# solution: dijkstra's algorithm using a priority queue (implemented using an array and min_by)
def dijkstra(neighbors,s)
    q = neighbors.keys
    dist = Hash.new(Float::INFINITY)
    dist[s] = 0
    
    until q.empty? do
        u = q.min_by {|v| dist[v]}
        q.delete(u)
        neighbors[u].each do |v|
            dist[v] = [dist[u]+6,dist[v]].min
        end
    end
    
    return dist
end

q = gets.strip.to_i
q.times do
    n, m = gets.strip.split.map &:to_i
	
    neighbors = Hash.new([])
    m.times do
        u, v = gets.strip.split.map &:to_i
		
        neighbors[u] += [v]
        neighbors[v] += [u]
    end
    s = gets.strip.to_i
    dists = dijkstra(neighbors,s)
    puts ((1..n).to_a - [s]).map {|v| dists[v] != Float::INFINITY ? dists[v] : -1 }.join(' ')
    
end
