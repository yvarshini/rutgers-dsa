class Bipartite:
    def __init__(self, G):
        self.bipartite = True
        self.color = [False]*G.V
        self.marked = [False]*G.V
        self.edgeTo = [None]*G.V

        for v in range(G.V):
            if not self.bipartite:
                return
            if not self.marked[v]:
                self.dfs(G, v)
    
    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.bipartite:
                return
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.color[w] = not self.color[v]
                self.dfs(G, w)
            elif self.color[v] == self.color[w]:
                self.bipartite = False

from graph import Graph

if __name__ == "__main__":
    # absolute path for g1: r'/Users/varshiniyanamandra/Desktop/Fall 2022/DSA/HW11/graph.txt'
    g1 = Graph(filename = "graph.txt")
    # absolute path for g2: r'/Users/varshiniyanamandra/Desktop/Fall 2022/DSA/HW11/graph1.txt'
    g2 = Graph(filename = "graph1.txt")
    
    g1_bp = Bipartite(g1)
    g2_bp = Bipartite(g2)

    print("Is situation 1 possible?")
    print(g1_bp.bipartite)
    print("Is situation 2 possible?")
    print(g2_bp.bipartite)