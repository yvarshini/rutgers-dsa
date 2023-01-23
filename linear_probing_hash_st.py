class LinearProbingHashST:
    INIT_CAPACITY = 11

    def __init__(self, m=None, max_load = 0.50):
        self.n = 0  
        self.m = m or LinearProbingHashST.INIT_CAPACITY  # hash table size
        self.max_load = max_load
        self.keys = [None for _ in range(self.m)]
        self.vals = [None for _ in range(self.m)]

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.m

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

    def get(self, key):
        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1) % self.m

        return None

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        # double table size if 50% full
        if (self.n /self.m  >=  self.max_load):
            self.resize(2 * self.m)

        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.vals[i] = val
                return 
            i = (i + 1) % self.m
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def delete(self, key):
        if not self.contains(key):
            return

        i = self.hash(key)
        while self.keys[i] != key:
            i = (i + 1) % self.m
        self.keys[i] = None
        self.vals[i] = None

        # rehash all keys in same cluster
        i = (i + 1) % self.m
        while self.keys[i] is not None:
            key_to_hash = self.keys[i]
            val_to_hash = self.vals[i]
            self.keys[i] = None
            self.vals[i] = None
            self.n -= 1
            self.put(key_to_hash, val_to_hash)
            i = (i + 1) % self.m

        self.n -= 1
        # halves size of array if it's 12.5% full or less
        if self.n > 0 and self.n <= self.m / 8:
            self.resize(self.m / 2)

    def resize(self, capacity):
        tmp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self.keys[i] is not None:
                tmp.put(self.keys[i], self.vals[i])

        self.m = tmp.m
        self.keys = tmp.keys
        self.vals = tmp.vals
    
    def load_factor(self):
        return self.n / self.m 

if __name__ == '__main__':

    st = LinearProbingHashST(10)
    i = 0
    for key in "ABCDE":
        st.put(key, i)
        i += 1

    for s in st.keys:
        if s:
            print(s + " " + str(st.get(s)))
    print()
            
    for i in range(st.m):
        if st.keys[i]:
            print(i, st.keys[i], end = " ")
            if st.keys[i] is None:
                print()
            else:
                print(hash(st.keys[i]) & 0x7FFFFFFF)
        else: print(i)
