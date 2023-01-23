"""
 *  Execution    python bread_first_paths.py G s
 *  Dependencies: Graph.java Queue.java Stack.java  
 *  Data files:   tinyCG.txt
 *
 *               
 *
 *  Run breadth first search on an undirected graph.
 *  Runs in O(E + V) time.
 *
"""

from stack import Stack
from graph import Graph
from queueArrayBased import Queue

class BreadthFirstPaths:

    def __init__(self, G, s):
        self._marked = [False] * G.V
        self.edge_to = [None] * G.V
        self.s = s
        self.bfs(G, s)
    # time-complexity = O(V + E)

    def bfs(self, G, s):
        self._marked[s] = True
        queue = Queue()
        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            for w in G.adj[v]:
                if not self._marked[w]:
                    self.edge_to[w] = v
                    self._marked[w] = True
                    queue.enqueue(w)
    # time-complexity = O(V + E)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]
        path.push(self.s)
        return path
    # worst-case time-complexity = O(V) = O(N)
    
    def distTo(self, v): 
        # no changes were made to any methods outside this class for question 1A
        if not self.has_path_to(v):
            return "NC" # NC - Not Connected
        return len(self.path_to(v))-1
    # worst-case time-complexity = O(V) = O(N)
    
    def path_to_start(self, v):
        path_to_start = Stack()
        path = self.path_to(v)
        while path.is_empty() == False:
            path_to_start.push(path.pop())
        for x in path_to_start:
            if x == v:
                print(x, end = '')
            else:
                print('-%s' % x, end='')
        print()
    
    def has_path_to_start(self, v):
        if self.has_path_to(v):
            return True
        return False

class AllShortestPaths:

    def __init__(self, G, s):
        self.s = s
        self.g = G
        self.n = G.V
        self.m = [[None for _ in range(G.V)] for _ in range(G.V)]
        self.fillMatrix()

    def fillMatrix(self):
        for i in range(self.n-1):
            bfs = BreadthFirstPaths(self.g, i) # init takes O(V+E) time
            for j in range(i+1, self.n):
                self.m[i][j] = bfs.distTo(j) # distTo(j) takes O(V) time
            self.m[i] = [x for x in self.m[i] if x is not None]
    # space-complexity = O(V^2) = O(N^2)
    # worst-case time-complexity = O(V*[(V+E)+V^2])
    # if we assume E is in the order of V, time-complexity = O(V^3) = O(N^3)


    def distance(self, x: int, y: int):
        if x == y:
            return 0
        elif x < y:
            # return "This is greater"
            return self.m[x][y-x-1]
        else:
            # return "This is lesser"
            return self.m[y][x-y-1]
    # time-complexity for distance(x, y) alone = O(1) [the adjacency/distance matrix is already filled]

    def printTable(self):
        for x in range(self.n-1):
            print(x, self.m[x])
    # time-complexity for printTable() alone = O(1) [the adjacency/distance matrix is already filled]

# Question 3
class StaticUF:

    def __init__(self, G, s):
        self.g = G
        self.bfs = BreadthFirstPaths(G, s)
        # time-complexity = O(V + E)

    def find(self, p: int):
        while self.bfs.edge_to[p] != None:
            p = self.bfs.edge_to[p]
        return p
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)

if __name__ == '__main__':
    
    import sys
    # s = int(sys.argv[2])
    s = int(6)
    
    g = Graph(filename='tinyCG2.txt')
    # g = Graph(filename=sys.argv[1])

    bfs = BreadthFirstPaths(g, s)
    for v in range(g.V):
        if bfs.has_path_to(v):
            distance = -1
            print("%d to %d [%d]: " % (s, v, bfs.distTo(v)), end='')
            for x in bfs.path_to(v):
                if x == s:
                    print(x, end='')
                else:
                    print('-%s' % x, end='')
            print()
        else:
            print("%d and %d: not connected" % (s, v))
            
    print()            
    for v in range(g.V):
        print(v, end = ' ')
        bfs.path_to_start(v)
    print()

    # Question 2
    paths = AllShortestPaths(g, s) # does all the preprocessing during creation of the class object
    print(paths.distance(7, 5), end = '\n\n') # time-complexity is O(1) as it is retrieving an array element based on the index
    paths.printTable()
    print()

    # Question 3
    staticuf = StaticUF(g, s)
    print("Is {} found?: ".format(s), staticuf.find(s))
    print("Are 3 and 4 connected?: ", staticuf.connected(3, 4))
