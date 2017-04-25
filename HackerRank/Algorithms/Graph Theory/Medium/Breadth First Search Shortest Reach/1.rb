# solution: simple breadth-first-search through all nodes/edges of the graph starting at node s (essentially dijkstra's algorithm)
# Uses an adjacency matrix for the graph and a queue for storing the nodes to be searched
def bfs(g,s)
    q = []
    dists = Hash.new(Float::INFINITY)
    curr = s
    dists[curr] = 0
    
    #q += g[curr].each_index.select {|v| v != s && !dists.include?(v) && g[curr][v] == 1 }.map {|v| [curr,v] }
    g[curr].each.with_index {|e,v| q.push [curr,v] if v != s && e == 1 && !dists.include?(v)}
    while q.size > 0
    	prev,curr = q.shift
        dists[curr] = [6 + dists[prev],dists[curr]].min
        #q += g[curr].each_index.select {|v| v != s && !dists.include?(v) && g[curr][v] == 1 }.map {|v| [curr,v] }
        g[curr].each.with_index {|e,v| q.push [curr,v] if v != s && e == 1 && !dists.include?(v)}
        #prev,curr = q.shift
    end
    
    return dists
end

q = gets.strip.to_i
q.times do
    n, m = gets.strip.split.map &:to_i
    g = []
    n.times do
        g << [0]*n 
    end
    
    m.times do
        u, v = gets.strip.split.map { |x| x.to_i - 1 }
        g[u][v] = 1
        g[v][u] = 1
    end
    s = gets.strip.to_i - 1
    dists = bfs(g,s)
    puts ((0...n).to_a - [s]).map {|v| dists.include?(v) ? dists[v] : -1 }.join(' ')
    
end
