import random
# O(N) expected time
# O(N^2) worst-case time
def quickSelect(arr, k):
    '''
        Returns the k-th smallest element in list 'arr'
    '''
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)

    L = [x for x in arr if x < pivot]
    E = [x for x in arr if x == pivot]
    G = [x for x in arr if x > pivot]

    if k <= len(L):
        # k-th smallest is the k-th smallest in L
        return quickSelect(L, k)
    elif k <= len(L) + len(E):
        # k-th smallest element is the pivot
        return pivot
    else:
        # k-th smallest is j-th smallest in G
        j = k - len(L) - len(E)
        return quickSelect(G, j)