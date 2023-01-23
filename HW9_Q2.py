# Heap sort
def sink(a, i, length):
    while 2*i + 1 <= length:
        j = 2*i + 1
        if (j < length and a[j] < a[j + 1]):
            j += 1
        if a[i] > a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j

def heapSort(arr):
    N = len(arr)
    k = N//2
    while k >= 0:
        sink(arr, k, N-1)
        k -= 1
    while N > 0:
        arr[0], arr[N-1] = arr[N-1], arr[0]
        N -= 1
        sink(arr, 0, N-1)
    return arr

# Validate (x, y)
def validate_xy(s1, s2, k):
    # sort both arrays using heapSort - O(NlogN) for each array s1 and s2
    heapSort(s1)
    heapSort(s2)
    # return False if the maximum possible sum is less than k - O(1)
    if s1[-1] + s2[-1] < k:
        return False
    # return False if the minimum possible sum is greater than k - O(1)
    if s1[0] + s2[0] > k:
        return False
    # run a while loop to check for (x, y) in all other cases - O(N), as there are 2N comparisons in the worst case
    i, j = 0, len(s2)-1
    while i < len(s1) and j >= 0:
        if s1[i] + s2[j] == k:
            return True
        elif s1[i] + s2[j] > k:
            j -= 1
        else:
            i += 1
    return False
# time complexity = O(NlogN) worst-case
# space complexity = O(1) for heapSort

if __name__ == "__main__":
    a = [1, 5, 6, 3, 8, 5, 10]
    b = [-6, 2, 75, -40, 0, 8, 3]
    print("Can the sum be -32?", validate_xy(a, b, -32))
    print("Can the sum be 100?", validate_xy(a, b, 100))