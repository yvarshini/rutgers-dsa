# QUICK FIND (eager approach)
class qfUF:
    
    def __init__(self, n): # O(N)
        # keep track of the number of groups
        self.count = n
        # create a list of length n
        # each element is initialized with itself as id
        self.id = list(range(n))
    
    # return the id of p
    # which is the same as the group in which p resides
    def find(self, p): # O(1)
        return self.id[p]
    
    # check whether p and q are connected
    def connected(self, p, q): # O(1)
        return self.id[p] == self.id[q]

    # union of the elements in p's and q's groups
    def union(self, p, q): # O(N) for 1 union
        # nothing to do if they are already connected/ in the same group
        if self.connected(p, q):
            return
        # connect p and q if they are not already connected
        pId = self.find(p)
        qId = self.find(q)
        for i in range(len(self.id)):
            # change the id of all elements in p's group to qId
            if self.id[i] == pId:
                self.id[i] = qId
        # decrease the number of groups by 1
        self.count -= 1

# QUICK UNION (lazy approach)
class quUF:
    def __init__(self, n): # O(N)
        self.count = n
        self.id = list(range(n))

    # return the root of p
    def find(self, p): # O(N) for 1 find
        while self.id[p] != p:
            p = self.id[p]
        return p

    # check if p and q are connected 
    # by checking if they have the same root
    def connected(self, p, q): # O(N) because it relies on finding p and q
        return self.find[p] == self.find[q]

    # union of p and q by attach the root of p to the root of q
    def union(self, p, q): # O(N) becuse it relies on finding pId and qId
        pId = self.find(p)
        qId = self.find(q)
        # nothing to do if p and q already have the same root
        # which means that they are already connected
        if pId == qId:
            return
        # if p and q are not connected, change the root of p to the root of q
        self.id[pId] = qId
        # decrement count by 1 as the number of groups has decreased
        self.count -= 1

# WEIGHTED QUICK UNION
class weighted_QU_UF:

    def __init__(self, n): # O(N)
        self.count = n
        self.id = list(range(n))
        # initialize size of each node as 1
        self.size = [1 for _ in range(n)]

    # depth of any node is now, at maximum, log_n
    def find(self, p): # O(log_n)
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q): # O(log_n), as it depends upon finding p and q
        return self.find(p) == self.find(q)

    def union(self, p, q): # O(log_n) as it relies on finding p and q's roots
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.size[pId] < self.size[qId]:
            self.id[pId] = qId
            self.size[qId] += self.size[pId]
        else:
            self.id[qId] = pId
            self.size[pId] += self.size[qId]
        self.count -= 1

# WEIGHTED QUICK-UNION WITH PATH COMPRESSION
class UF:
    
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.size = [1 for _ in range(n)]

    # set the id of each examined root in the path to root
    # to the id of the root
    def find(self, p): # O(log*_n)
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def connected(self, p, q): # O(log*_n), as it depends upon finding p and q
        return self.find(p) == self.find(q)

    def union(self, p, q): # O(log*_n) as it relies on finding p and q's roots
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.size[pId] < self.size[qId]:
            self.id[pId] = qId
            self.size[qId] += self.size[pId]
        else:
            self.id[qId] = pId
            self.size[pId] += self.size[qId]
        self.count -= 1