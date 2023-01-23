import sys
from myqueue import Queue
from mystack import Stack

class Graph:

    def __init__(self, v, filename = None):
        if filename is None:
            self.V = v
            self.E = 0
            self.adj = {}
            for v in range(self.V):
                # creating adjacency list for every vertex
                self.adj[v] = set()
        else:
            infile = open(filename, 'r')
            self.V = int(infile.readline())
            self.E = int(infile.readline())
            self.adj = {}
            for v in range(self.V):
                self.adj[v] = set()
            for _ in range(self.E):
                # add edges read from the file
                v, w = infile.readline().split()
                self.add_edge(v, w)
            infile.close()

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        # add v to w's adjacency list and vice-versa
        self.adj[v].add(w)
        self.adj[w].add(v)
        # one edge has been added to the graph
        self.E += 1

class DFS:
    # total time for DFS = O(V + E)
    # space = O(V + E)
    def __init__(self, g, s):
        # time to initialize the arrays = O(V)
        # g is the graph object
        # s is the starting point

        # creating arrays of length equal to the number of vertices
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.s = s
        self.dfs(g, s)

    def dfs(self, g, v):
        # time to run actual dfs algorithm = O(E), 
        # which is the sum of the degrees of all vertices in the connected component
        self.marked[v] = True
        # visit all vertices adjacent to vertex v that have not been visited previously
        for w in g.adj[v]:
            if not self.marked[w]:
                # add v to the adjacecy list of w
                self.edgeTo[w] = v
                self.dfs(g, w)
    # marked[v] is true is v is connected to s
    # edgeTo[v] = previous vertex on path from s to v

    def hasPathTo(self, v):
        return self.marked[v]
    
    def path_to(self, v: int):
        if not self.hasPathTo(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            # go one step back until we reach s
            x = self.edgeTo[x]
        path.push(self.s)
        return path

# edges discovered from DFS(g, v) form a spanning tree of the connected component of v

class CC:

    def __init__(self, g):
        self.marked = [False] * g.V
        self.id = [0] * g.V # id of the component/group that a vertex belongs to
        self.count = 0 # number of groups in the connected component

        for s in range(g.V):
            # if the vertex does not already belong to a group, perform dfs
            if not self.marked[s]:
                self.dfs(g, s)
                # move on to the next group once dfs is done
                self.count += 1

    def dfs(self, g, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

class Cycle:

    def __init__(self, g):
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.has_cycle = False
        self.cycle = []
        for s in range(g.V):
            if not self.marked[s]:
                # dfs with checking for cycles
                self.dfs(g, s, s)

    def dfs(self, g, v, u):
        '''
            Parameters:
                g: graph
                v: starting vertex
                u: predecessor of v - to ensure that (u, v) and (v, u) are not identified as a cycle
        '''
        # mark v as visited
        self.marked[v] = True

        for w in g.adj[v]:
            # terminate dfs is cycle is found
            if self.has_cycle:
                return
            
            if not self.marked[w]:
                # add v to w's adjacency list if w has not been previously visited
                self.edgeTo[w] = v
                # (v, w) is already marked, so avoid having (w, v) marked as a cycle
                self.dfs(g, w, v)
            # don't mark it as a cycle if w is u
            elif w != u:
                # if w has been previously visited, we have found a cycle
                self.has_cycle = True
                # start at v, which is adjacent to w
                x = v
                while x != w:
                    # add all vertices encountered so far to the cycle, starting from v
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                # finally, add w and v to the list to finish the cycle
                self.cycle += [w, v]
                # since has_cycle has been marked true, dfs will stop executing in the next iteration

# g = Graph(0, "tinyG.txt")

# c = CC(g)
# for x in range(g.V):
#     print('{}: '.format(x), c.id[x])
# components = [0] * c.count
# for i in range(c.count):
#     components[i] = set()

# for i in range(g.V):
#     components[c.id[i]].add(i)

# for i in range(c.count):
#     print(components[i])

class BreadthFirstPaths:

    def __init__(self, g, s):
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.s = s
        self.bfs(g, self.s)

    def bfs(self, g, s):
        # mark s as visited
        self.marked[s] = True
        q = Queue()
        q.enqueue(s)

        while not q.is_empty():
            # remove the first element in the queue
            v = q.dequeue()
            for w in g.adj[v]:
                if not self.marked[w]:
                    # add v to w's adjacency list
                    self.edgeTo[w] = v
                    # mark w as visited
                    self.marked[w] = True
                    # add w to the queue
                    q.enqueue(w)
    
    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        '''
            Returns shortest path from s to v in O(V + E) time
        '''
        # return empty if v is not connected to s
        if not self.marked[v]:
            return
        # path = Stack()
        path = []
        x = v
        while x != self.s:
            # path.push(x)
            path.append(x)
            x = self.edgeTo[x]
        # path.push(self.s)
        path.append(self.s)

        # reverse path if path is a list and not stack
        for i in range(len(path)//2):
            path[i], path[len(path) - 1 - i] = path[len(path) - 1 - i], path[i]

        return path
        
g = Graph(0, "undirectedGraphs/tinyCG.txt")
bfs = BreadthFirstPaths(g, 0)
print(bfs.pathTo(3))