# basic insertion sort
# no half swaps
# O(N^2) time
# O(1) auxiliary space
def insertionSort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                j -= 1

a = [8, 1, 4, 3, 7, 5, 2]
insertionSort(a)
print(a)
