from tempfile import TemporaryFile


class Node:
    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.N = N
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def size(self):
        return self._size(self.root)
    def _size(self, x):
        if x is None:
            return 0
        return x.N
    def get(self, key):
        return self._get(self.root, key)
    def _get(self, x, key):
        if x is None:
            return
        if x.key > key:
            return self._get(x.left, key)
        elif x.key < key:
            return self._get(x.right, key)
        else:
            return x.val
    def put(self, key, val):
        self.root = self._put(self.root, key, val)
    def _put(self, x, key, val):
        if x is None:
            return Node(key, val, 1)
        if x.key > key:
            x.left = self._put(x.left, key, val)
        elif x.key < key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, x, key):
        if x is None:
            return None
        if x.key > key:
            x.left = self._delete(x.left, key)
        elif x.key < key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x
    def delete_min(self):
        self.root = self._deleteMin(self.root)
    def _deleteMin(self, x):
        if x.left is None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x
    def is_empty(self):
        return self.root is None
    def in_order(self):
        return self._inorder(self.root)
    def _inorder(self, root):
        if root is None:
            return []
        return self._inorder(root.left) + [root.key]+self._inorder(root.right)
    
    ### Q1
    def getPathLength(self, given_node):
        count = 0
        ptr = self.root
        try:
            while self.root.N != 0:
                if given_node == ptr.key:
                    return count
                elif given_node < self.root.key:
                    ptr = ptr.left
                    count += 1
                else:
                    ptr = ptr.right
                    count += 1
        except:
            return None

    ### Q2
    def calculateSize(self):
        return self._calculateSize(self.root)

    def _calculateSize(self, root):
        count = 0
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self._calculateSize(root.left) + 1 + self._calculateSize(root.right)

        # Time complexity = O(N)
        # Space complexity = O(1)

    def validateSizeCounts(self):
        if self._validateSizeCounts(self.root) is None:
            return True
        else:
            return False
    
    def _validateSizeCounts(self, root):
        if root is None:
            return
        if self._calculateSize(root) != root.N:
            print(root.key)
        self._validateSizeCounts(root.left)
        self._validateSizeCounts(root.right)

        # Worst-case time complexity = O(N), which is due to the function _calculateSize()
        # Worst-case space complexity = O(1)

    ### Q3
    def validateSymmetricOrder(self):
        return self._validateSymmetricOrder(self.root, '1', 'a')

    def _validateSymmetricOrder(self, root, min, max):
        if root == None:
            return True
        if (root.key <= min) or (root.key >= max):
            return False
        return self._validateSymmetricOrder(root.left, min, root.key) and self._validateSymmetricOrder(root.right, root.key, max)

    # Worst-case running time = O(N)
    # Worst-case auxiliary space = O(1)

    ### Q4
    def toList(self):
        res = [None]
        self._toList(self.root, res, 1)
        return res

    def _toList(self, root, res, i):
        if root is None:
           return None
        try:
            res[i] = root.key
        except:
            res.extend([None]*i)
            res[i] = root.key
        self._toList(root.left, res, 2*i)
        self._toList(root.right, res, 2*i + 1)
        # Worst-case time complexity = O(N)
        # Worst-case space complexity = O(2^N)

    def search(self, key):
        res = [x for x in self.toList() if x != None and x == key]
        if res != []:
            return True
        return False
        # The worst-case time complexity is the time-complexity of self.toList(), which is O(N)
        # The worst-case auxiliary space complexity is the space complexity to self.toList(), which is O(N)

    ### Q5
    def bottom_up_traversal(self):
        res = [x for x in self.toList() if x != None]
        n = len(res)
        bottom_up = [0]*n
        for i in range(n):
            bottom_up[i] = res[n-1-i]
        return bottom_up

        # Worst-case time complexity = O(N)
        # Worst-case space complexity = O(N)

if __name__ == '__main__':
    st = BST()
    # for key in "ighmqlcaz".upper():
    for key in "jhimpkca".upper():
        st.put(key, 0)
    print("BST in order")
    print(st.in_order())

    pathLength = st.getPathLength('A')
    print("Q1: pathLength")
    print(pathLength)

    print("Q2: validateSizeCounts")
    print(st.validateSizeCounts())
    print("Size of the whole tree")
    print(st.calculateSize())

    print("Q3: validateSymmetricOrder")
    print(st.validateSymmetricOrder())

    x = st.toList()
    print("Q4: toList")
    print(x)
    print(st.search('G'))

    print("Q5: bottom-up traversal")
    print(st.bottom_up_traversal())