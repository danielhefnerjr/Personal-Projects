# Enter your code here. Read input from STDIN. Print output to STDOUT

def getComponent(g,v)
    component = [v]
    q = []
    q += g.each_index.select { |i| !component.include?(i) && !q.include?(i) && g[v][i] == 1}
    while !q.empty?
        curr = q.shift
        component << curr
        q += g.each_index.select { |i| !component.include?(i) && !q.include?(i) && g[curr][i] == 1}
    end
    
    component
end

def getAllComponents(g)
    components = []
    for v in 0...g.size
        if !components.flatten.include? v
            components << getComponent(g,v)
        end
    end
    
    components
end

def removeEdge(g,e)
    u,v = e
    g[u][v] = 0
    g[v][u] = 0
    
    g
end

def addEdge(g,e)
    u,v = e
    g[u][v] = 1
    g[v][u] = 1
    
    g
end

def searchForMax(g,edges,c)
    if getAllComponents(g).any? { |x| x.size.odd?} 
        return 0
    end
    
    ret = c
    for i in 0...edges.size
        ret = [ret,searchForMax(removeEdge(g,edges[i]),edges[0...i] + edges[i+1...edges.size],c+1)].max
        #puts edges[i].join ' '
        addEdge(g,edges[i])
    end
    
    ret
end
n,m = gets.strip.split.map &:to_i
g = []
n.times do
    g << [0]*n
end
edges = []
m.times do
    u,v = gets.strip.split.map {|x| x.to_i - 1 } 
    g[u][v] = 1
    g[v][u] = 1
    edges << [u,v]
end
puts searchForMax(g,edges,0)
