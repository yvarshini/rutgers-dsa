def mysort(arr):
    n = len(arr)
    count = 0
    res = []*pow(n, 2)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                res.append((arr[i], arr[j]))
                count += 1
    return res, count

# time complexity = O(N^2)
# space complexity = O(N^2)

def in_place_insertion_sort(arr):
    n = len(arr)
    res_arr = []*n*n    # O(N^2) work here to avoid potential resizing of array while inside the loop
    count = 0
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            res_arr.append((arr[j], key))
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = key

    return count, res_arr

    # time complexity = O(N^2)
    # space compexity = O(1)

def sink(arr, i, length):
    while(2*i+1 <= length):
        j = 2*i + 1
        if j < length and arr[j] < arr[j+1]:
            j += 1
        if arr[i] > arr[j]:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i = j

def heapsort(arr, n):
    count = 0
    k = n//2
    # heapify the array
    while k >= 0:
        sink(arr, k, n-1)
        k -= 1

    while n > 0:
        arr[0], arr[n-1] = arr[n-1], arr[0]
        n -= 1
        sink(arr, 0, n-1)

    return arr, count