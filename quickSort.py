def basicPartition(arr, pivot):
    L, E, G = []
    while len(arr) > 0:
        x = arr.pop()
        if x > pivot:
            G.append(x)
        elif x == pivot:
            E.append(x)
        else:
            L.append(x)
    return L, E, G

# QUICKSORT
# O(NlogN) time amortized - probabilistic guarantee
# O(N^2) time worst case
# O(logN) space for in-place implementation
def partition(arr, lo, hi):
    pivot = arr[hi]
    left, right = lo, hi - 1

    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        
    arr[left], arr[hi] = arr[hi], arr[left]
    return left

def inplaceQuickSort(arr, lo, hi):
    if lo >= hi:
        return
    
    pivot = partition(arr, lo, hi)
    
    inplaceQuickSort(arr, lo, pivot - 1)
    inplaceQuickSort(arr, pivot + 1, hi)

import random
a = [1, 4, 3, 7, 5, 2]
random.shuffle(a)
# print(a)
# inplaceQuickSort(a, 0, len(a) - 1)
# print(a)

# THREE WAY QUICKSORT
def quickSort(arr, lo, hi):
    if lo >= hi:
        return

    lt, gt = lo, hi
    i = lo + 1
    pivot = arr[lo]

    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    quickSort(arr, lo, lt - 1)
    quickSort(arr, gt + 1, hi)

quickSort(a, 0, len(a) - 1)
print(a)