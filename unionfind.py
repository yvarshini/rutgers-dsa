class UF:

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # weighted quick-union
    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]] # path compression
            p = self.id[p]
        return p

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        self.id[pId] = qId
        self.count -= 1

class StaticUF:

    def __init__(self, n):
        self.p = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, p):
        while p != self.p[p]:
            self.p[p] = self.p[self.p[p]]
            p = self.p[p]
        return p
    
    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q:
            return True
        if self.rank[root_p] > self.rank[root_q]:
            self.p[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.p[root_p] = root_q
        else:
            self.p[root_p] = root_q
            self.rank[root_q] += 1
        return False

# Question 3
class StaticUF:

    def __init__(self, n):
        self.p = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, p):
        while p != self.p[p]:
            self.p[p] = self.p[self.p[p]]
            p = self.p[p]
        return p
    
    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q:
            return True
        if self.rank[root_p] > self.rank[root_q]:
            self.p[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.p[root_p] = root_q
        else:
            self.p[root_p] = root_q
            self.rank[root_q] += 1
        return False
