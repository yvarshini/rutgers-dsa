class directedGraph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]
        self.indegree = [0] * N
        for (src, dest) in edges:
            # add directed edge
            self.adjList[src].append(dest)
            self.indegree[dest] = self.indegree[dest] + 1

def findAllTopologicalOrders(g, path, marked, n, res = None):
    if res is None:
        res = []
    for v in range(n):
        # proceed only if in-degree of vertex is 0 and it is not yet visited
        if g.indegree[v] == 0 and not marked[v]:
            # for every adjacent vertex u of v, reduce in-degree of u by 1
            for u in g.adjList[v]:
                g.indegree[u] = g.indegree[u] - 1
            # include current vertex in the path and mark it as visited
            path.append(v)
            marked[v] = True

            findAllTopologicalOrders(g, path, marked, n, res)

            for u in g.adjList[v]:
                g.indegree[u] = g.indegree[u] + 1
            path.pop()
            marked[v] = False
    
    if len(path) == n:
        # print(path) - to get a list of all Topological Orders of a graph
        res.append([x for x in path])
    return res

def validTopologicalOrder(g: directedGraph, order):
    n = len(g.adjList)
    marked = [False]*n
    path = []
    x = findAllTopologicalOrders(g, path, marked, n)

    if order in x:
        return True
    return False

# creating graph
data = open("graphT.txt", "r")
n = int(data.readline())
e = int(data.readline())
edges = []*e
for _ in range(e):
    x, y = data.readline().split()
    edges.append((int(x),int(y)))
g = directedGraph(edges, n)

o1 = [3, 6, 0, 5, 2, 1, 4]
o2 = [4, 3, 6, 0, 5, 2, 1]
o3 = [3, 6, 0, 5, 1, 4, 2]
print("Is o1 a topological sort of the given graph?")
print(validTopologicalOrder(g, o1))
print("Is o2 a topological sort of the given graph?")
print(validTopologicalOrder(g, o2))
# extra test case - o3
print("Is o3 a topological sort of the given graph?")
print(validTopologicalOrder(g, o3))