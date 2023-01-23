class LinearProbingHashST:

    # Q1.3 - Revised methods
    # delete - changed the code to simply replace the original key with "tombstone"; no rehashing required
    # put - added condition to insert a key-value pair if the key is "tombstone"

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
        while self.keys[i] is not None and self.keys[i] != "tombstone": # changed to include "tombstone"
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
        i = 0
        while self.keys[i] != key:
            i += 1
        self.keys[i] = "tombstone"
        self.n -= 1

        # i = self.hash(key)
        # while self.keys[i] != key:
        #     i = (i + 1) % self.m
        # self.keys[i] = None
        # self.vals[i] = None

        # # rehash all keys in same cluster
        # i = (i + 1) % self.m
        # while self.keys[i] is not None:
        #     key_to_hash = self.keys[i]
        #     val_to_hash = self.vals[i]
        #     self.keys[i] = None
        #     self.vals[i] = None
        #     self.n -= 1
        #     self.put(key_to_hash, val_to_hash)
        #     i = (i + 1) % self.m

        # self.n -= 1
        # # halves size of array if it's 12.5% full or less
        # if self.n > 0 and self.n <= self.m / 8:
        #     self.resize(self.m / 2)

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

    # Q1.1
    def get_clusters(self):
        clusterSize = []
        stop = 0
        size = 0
        while stop != self.m:
            if self.keys[stop] != None:
                size += 1
                stop += 1
            else:
                if self.keys[stop-1] != None and size != 0:
                    clusterSize.append(size)
                    size = 0
                stop += 1
        if size != 0:
            clusterSize.append(size)
            
        if self.keys[0] != None and self.keys[-1] != None:
            clusterSize[-1] += clusterSize[0]
            clusterSize.remove(clusterSize[0])

        return clusterSize

    def expected_probes_for_new_insert(self, key, value):
        old_clusters = self.get_clusters()
        resize = False
        if (self.n/self.m >= self.max_load):
            resize = True
        self.put(key, value)
        
        new_clusters = self.get_clusters()
        # If the table is resized, calculating the expected value of the total number of probes, 
        # including the ones to insert old elements into the new table
        if resize:
            sum = 0
            for currsize in new_clusters:
                if currsize == 1:
                    sum += currsize
                else:
                    sum += 1
                    for i in range(2, currsize):
                        sum += i//2
            return sum

        if len(new_clusters) != len(old_clusters):
            if len(new_clusters) == len(old_clusters) - 1:
                for i in range(len(new_clusters)):
                    if new_clusters[i] != old_clusters[i]:
                        return new_clusters[i]//2
            return 1
        else:
            for i in range(len(new_clusters)):
                if new_clusters[i] != old_clusters[i]:
                    if new_clusters[i] != 1:
                        return new_clusters[i]//2
                    else:
                        return 1

    # Q1.2
    def theoretical_probes_for_insert(self, key, value):
        self.put(key, value)
        ans = 0.5*(1 + (1/(1-(self.n/self.m)))) + 1
        return ans
        # This does not match with the expected value calculated in Q1.1 when the table is resized

if __name__ == '__main__':

    st = LinearProbingHashST(10)
    i = 0
    for key in "ABCD":
        st.put(key, i)
        i += 1
    # print(st.keys)
    # for s in st.keys:
    #     if s:
    #         print(s + " " + str(st.get(s)))
    # print()
            
    # for i in range(st.m):
    #     if st.keys[i]:
    #         print(i, st.keys[i], end = " ")
    #         if st.keys[i] is None:
    #             print()
    #         else:
    #             print(hash(st.keys[i]) & 0x7FFFFFFF)
    #     else: print(i)

    # print("Expectation", st.expected_probes_for_new_insert("G", 7))
    # print("Theoretical", st.theoretical_probes_for_insert("G", 7))
    st.delete("B")
    st.put("G", 7)

    for i in range(st.m):
        if st.keys[i]:
            print(i, st.keys[i], end = " ")
            if st.keys[i] is None:
                print()
            else:
                print(hash(st.keys[i]) & 0x7FFFFFFF)
        else: print(i)
