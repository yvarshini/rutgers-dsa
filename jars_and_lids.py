from random import shuffle, randint
import sys
import queue

# quickSort time complexity = O(N^2) worst case, with NlogN probabilistic guarantee
# quickSort space complexity = O(logN)
def quickSort(arr, lo, hi):
    if lo >= hi:
        return
    lt = lo
    gt = hi
    i = lo + 1
    pivot = arr[lo]
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    quickSort(arr, lo, lt - 1)
    quickSort(arr, gt + 1, hi)

def modifiedQuickSort():
    
    pass

def arrange(jars, lids):
    """
    This method cannot compare any lid to any other lid and cannot 
    compare any jar to any other jar.
    The mehod can compare a jar to a lid an vice versa.
    For example, jar[i] < jar[j] is not allowed but jar[i] < lid[j] is allowed
    """

    pass

jars = list({randint(0, sys.maxsize) for i in range(15)})
lids = list(jars)

shuffle(jars)
shuffle(lids)

print(lids)
print(jars)

arrange(jars, lids)

print(jars == lids)
