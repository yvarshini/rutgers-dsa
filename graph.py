"""
   Execution:    python graph.py input.txt
   Data files:   tinyG.txt
 
   A graph, implemented using an array of sets.
   Parallel edges and self-loops allowed.
 
   % python graph.py < tinyG.txt
   13 vertices, 13 edges 
   0: 6 2 1 5 
   1: 0 
   2: 0 
   3: 5 4 
   4: 5 6 3 
   5: 3 4 0 
   6: 0 4 
   7: 8 
   8: 7 
   9: 11 10 12 
   10: 9 
   11: 9 12 
   12: 11 9 
 
 """
import sys

class Graph:

    def __init__(self, v=None, filename=None):
        if filename is None:
            self.V = v
            self.E = 0
            self.adj = {}
            for v in range(int(self.V)):
                self.adj[v] = set()
        else:
            infile = open(filename, "r")
            self.V = int(infile.readline())
            self.E = int(infile.readline())
            
            self.adj = {}
            for v in range(self.V):
                self.adj[v] = set()
            for _ in range(self.E):
                v, w = infile.readline().split()
                self.add_edge(v, w)            
            infile.close()            

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                   for w in self.adj[v])) for v in range(self.V))
        return s

 
    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_deg = 0
        for v in self.V:
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count

if __name__ == '__main__':
    g = Graph(None, sys.argv[1])

    print(g)
    
