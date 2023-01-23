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
        
        return self._inorder(root.left) +[root.key]+self._inorder(root.right)

    def inorder_with_count(self, root, sizeCountList):
        if root is None:
            return []
        self.inorder_with_count(root.left, sizeCountList) 
        sizeCountList.append(root.N)
        self.inorder_with_count(root.right, sizeCountList)
        
    def getPathLength(self, x, key, count):
      if x is None:
        return None
      if x.key == key:
        return count
      elif x.key>key:
        return self.getPathLength(x.left, key, count+1)
      elif x.key<key:
        return self.getPathLength(x.right, key, count+1)

    def getNodeSize(self, root, modifiedList, sizeCount, inOrderList):
      if root == None:
        return
      self.getNodeSize(root.left, modifiedList[:modifiedList.index(root.key)]
 , sizeCount, inOrderList)
      i = inOrderList.index(root.key)
      sizeCount[i] = len(modifiedList)
      self.getNodeSize(root.right, modifiedList[modifiedList.index(root.key)+1:], sizeCount, inOrderList)

    def validateSizeCount(self, givenSize, calculatedSize):
      #The worst case time complexity would be based on getNodeSize function which is O(N).
      #The Worst case space complexity would be O(n)
      if givenSize == calculatedSize:
        return True
      else:
        return False

    def validateSymmetric(self, sizeCountList):
      #The sizeCountList represents the size of each node in a inorder traversal. 
      if sizeCountList == sizeCountList[::-1]:
        return 'The Tree is Symmetric'
      else:
        return 'The Tree is not Symmetric'

    def toList(self, root, L, k):
      #The Worst case space complexity is O(n)
        if root is None:
            return None
        try:
          L[k] = root.key
        except Exception:
          L.extend([None]*k)
          L[k] = root.key
        self.toList(root.left, L, 2*k)
        self.toList(root.right, L, (2*k) +1)

    def searchKey(self, treesList, key):
      #The worst case time complexity is O(n) and space is O(1).
      for i in treesList:
        if i==key:
          return 'Key Found'

      return 'Key Not Found'

    def bottom_up_traversal(self, treesList):
      #The Worst case time complexity would be (making tree into a list) would be O(n)
      #The Worst case space complexity is O(2^N) 
      #Using the conversion of TreesList to print the bottom up traversal
      print([x for x in treesList[::-1] if x!=None])

     
if __name__ == '__main__':
    st = BST()

    for key in "ighmqlbtscaz".upper():
    # for key in "jhimpkca".upper():
        st.put(key, 0)

    inOrderList=st.in_order()
    givenSizeCount=[]
    st.inorder_with_count(st.root, givenSizeCount) #Helper function to get size count of each node in a tree
  
    print("Q1: getPathLength")
    print(st.getPathLength(st.root,"H",0))
    print("Q2: Validating Size Count: True or False")
    #Here I am assuming that the given count in the tree node is wrong, therefore calculating my own tree size count for each note
    calculatedSizeCount = [None] * len(inOrderList)
    st.getNodeSize(st.root, inOrderList, calculatedSizeCount, inOrderList) #Helped function to return the node size in the 
    print(st.validateSizeCount(givenSizeCount, calculatedSizeCount))
  
    print("Q3: Validating if the tree is symmetric")
    print(st.validateSymmetric(givenSizeCount))
  
    print("Q4: Converting a tree to a list")
    treesList = [None] 
    st.toList(st.root, treesList, 1)
    print(treesList)
    print(st.searchKey(treesList,st.root.key))
  
    print("Q5: Bottom up traversal")
    st.bottom_up_traversal(treesList)
