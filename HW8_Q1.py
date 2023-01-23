count = 0

def merge(lefthalf, righthalf, arr, pr: bool):
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

def mergeSort(arr, pr: bool):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf, pr)
        mergeSort(righthalf, pr)

        merge(lefthalf, righthalf, arr, pr)

# Q1
# Goal: O(NlogN) time complexity
def count_transpositions(arr):
    mergeSort(arr, pr = False)
    return count

# time complexity = O(NlogN)
# space complexity = O(1)

# Q2
# Goal: O(N + k) time complexity
def print_transpositions(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            print((arr[j], key))
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# time complexity = O(N + k)
# space complexity = O(1)

a = [8, 4, 2, 1]
a = [10, 4, 6, 3, 8, 2]

# Q1
print(count_transpositions(a.copy())) # Using a.copy() in order to keep the original list unsorted for use in Q2

# Q2
print_transpositions(a)
