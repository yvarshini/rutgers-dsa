class Digraph:

    def __init__(self, v = 0, filename: str = None):
        if filename is None:
            self.V = v
            self.E = 0
            self.name = None
            self.adj = {}
            # create empty sets for adjacency lists
            for v in range(self.V):
                self.adj[v] = set()
        else:
            data = open(filename, 'r')
            self.V = data.readline()
            self.E = data.readline()
            self.name = str(filename)
            self.adj = {}
            for v in range(self.V):
                self.adj[v] = set()
            for i in range(self.E):
                v, w = data.readline().split()
                self.add_edge(v, w)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        # increment total number of edges by 1
        self.E += 1

    def reverse(self):
        '''
            Reverse every edge in a digraph to obtain the reverse of the digraph
        '''
        R = Digraph(self.V, self.name)
        v = 0
        # iterate over all vertices, starting from vertex '0'
        while v < self.V:
            for w in self.adj[v]:
                R.add_edge(w, v)
            # increment vertex number by 1
            v += 1
        return R

    def __str__(self):
        s = "%d vertices, %d edges \n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w) for w in self.adj[v])) for v in range(self.V))
        return s

class DFS: # same as the one for undirected graphs

    def __init__(self, g, s):
        self.marked = [False] * g.V
        self.edgeTo = [None] * g.V
        self.count = 0
        self.dfs(g, s)

    def dfs(self, g, v):
        # mark vertex v as visited
        self.marked[v] = True
        self.count += 1
        for w in g.adj[v]:
            if not self.marked[w]:
                # v has an edge leading to w
                self.edgeTo[w] = v
                self.dfs(g, w)

class BFS:

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

