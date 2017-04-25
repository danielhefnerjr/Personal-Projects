require "C:/Users/Daniel/Documents/Personal Projects/Algos/lists/ruby/minprioqueue.rb"


def dijkstra(source, edges, weights)
    visited = Hash.new false
    distances = Hash.new Float::INFINITY
    previous = {}
    
    q = MinPriorityQueue.new
    q.push Element.new(source,0)
    
    visited[source] = true
    distances[source] = 0
    
    while !q.empty? do
        u = q.pop.val
        visited[u] = true
        
        edges[u].reject { |v| visited[v] }.each do |v| 
            alt = distances[u] + weights[u][v]
            if alt < distances[v]
                distances[v] = alt
                previous[v] = u
            end
            q.push(Element.new(v,distances[v]))
        end
        
    end
    
    return distances, previous
end

n = gets.strip.to_i
edges = Hash.new {|h,k| h[k] = []}
weights = (n+1).times.map { Array.new(n+1,0) }
n.times do
    v1,v2,w = gets.strip.split.map &:to_i 
    edges[v1] << v2
    edges[v2] << v1
    weights[v1][v2] = weights[v2][v1] = w
end

distances,previous = dijkstra(1,edges,weights)
