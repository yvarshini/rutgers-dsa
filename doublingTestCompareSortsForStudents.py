from time import time
from random import randint 

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# modified insertion sort that swaps across multiple passes, with t-th passing having exchange distance n//k^t
def modifiedInsertionSort(arr, k):
    if k == 1:
        return ("Error: k can not be 1. Please enter a number greater than 1")
    n = len(arr)//k
    # keep passes going until n becomes <= 1
    while n > 1:
        for i in range(n, len(arr)):
            key = arr[i]
            j = i - n
            while j >= 0 and key < arr[j]:
                arr[j+n] = arr[j]
                j -= n
            arr[j+n] = key
        # divide n by k to reduce the exchange distance for the next pass
        n = n//k
    # final pass when n becomes either 0 or 1
    if n <= 1:
        insertionSort(arr)

INITIAL_SIZE = 1000
size = INITIAL_SIZE
NUMBER_OF_TRIALS = 5
# k should be greater than 1 - n//k will be the distance of the swaps in the first pass of modifiedInsertionSort
k = int(pow(size, 0.5))

print("k is", k)
print("Trial\tN\t\tIns\t\tGap\t\ty==z")
for i in range(NUMBER_OF_TRIALS):
    x = [randint(1, size) for _ in range(size)]
    y = list(x)
    z = list(x)
   
    start  = time()
    #sort #1 here
    insertionSort(y)
    elapsedTime = time() - start

    start  = time()
    # sort #2 here
    modifiedInsertionSort(z, k)
    elapsedTime1 = time() - start
         
    print("%1d %11s \t\t%.2f \t\t%.2f" % (i+1, "{:,}".format(size), elapsedTime, elapsedTime1), end= '\t\t')
    print(y==z)    
    size *= 2
    
