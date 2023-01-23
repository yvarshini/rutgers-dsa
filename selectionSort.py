# selection sort implementation using lists
# can also be implemented using Priority Queues with same time and space-complexities
# O(N^2) time
# O(N) auxiliary space
def selectionSort(arr):
    for i in range(len(arr)):
        temp = arr.index(min(arr[i:]))
        a[i], a[temp] = a[temp], a [i]

a = [1, 4, 3, 7, 5, 2]
selectionSort(a)
print(a)