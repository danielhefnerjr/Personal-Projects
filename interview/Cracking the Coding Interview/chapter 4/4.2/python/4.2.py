from collections import defaultdict

class Graph:
    def __init__(self,connections=[],directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        if connections:
            self.add_connections(connections)

    def add_connections(self,connections):
        for node1, node2 in connections:
            self.add(node1,node2)

    def add(self,node1,node2):
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)

    def remove(self,node):
        for n, connections in self.graph.iteritems():
            if n in connections:
                connections.remove(n)

        if node in self.graph.keys():
            del self.graph[node]

    def isPath(self,node1,node2):
        q = [node1]

        while q:
            n1 = q[0]
            if n1 == node2:
                return True

            q.extend(self.graph[n1])
            del q[0]
                
        return False

connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
G = Graph(connections,True)
print(G.isPath('A','D')) # true
print(G.isPath('B','A')) # false
print(G.isPath('A','F')) # false
