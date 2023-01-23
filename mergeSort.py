# O(NlogN) time
# O(N) auxiliary space (?)

def merge(lefthalf, righthalf, arr):
    i, j, k = 0, 0, 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1
    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1
    
    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        merge(lefthalf, righthalf, arr)

a = [1, 4, 3, 7, 5, 2]
mergeSort(a)
print(a)