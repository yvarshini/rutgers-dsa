count = 0

def merge(lefthalf, righthalf, arr):
    global count
    i, j, k = 0, 0, 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            count += len(lefthalf) - i
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

# Q1
# Goal: O(NlogN)
def transposition_count(arr):
    global count
    mergeSort(arr)
    print(count)
    count = 0

# Q2
# Goal: O(N + k)


a = [8, 4, 2, 1]
# a = [10, 4, 6, 3, 8, 2]

transposition_count(a)
