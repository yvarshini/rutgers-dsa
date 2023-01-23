def factorial(n: int):
    '''
        Return the factorial of given number n
    '''
    if n < 1:
        return("Error: n has to be a natual number")
    if n == 1:
        return n
    return n*factorial(n-1)

def reverse(seq, start, stop):
    '''
        Reverse elements in implicit slice seq[start:stop]
    '''
    if start < stop - 1:
        seq[start], seq[stop - 1] = seq[stop - 1], seq[start]
        reverse(seq, start + 1, stop - 1)

def binarySearch(data, target, low, high):
    '''
        Check if given value "target" is in the data (sorted)
    '''
    if low >= high:
        return False
    mid = (low + high)//2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        # recursion if the midpoint of data is greater than target
        return binarySearch(data, target, low, mid - 1)
    else:
        # recursion if the midpoint of data is lesser than target
        return binarySearch(data, target, mid + 1, high)

def isPalindrome(str, start, stop):
    if start >= stop:
        return True
    if str[start] != str[stop]:
        return False
    return isPalindrome(str, start + 1, stop - 1)

def powerSet(a: list):
    if len(a) == 0:
        return [[]]
    partialSubsets = powerSet(a[1:])
    allSubsets = []
    for subset in partialSubsets:
        allSubsets.append(subset)
        allSubsets.append([a[0]] + subset)
    return allSubsets

def bad_fibonacci(n: int):
    if n < 0:
        return("error: n must be a whole number")
    if n <= 1:
        return n
    return bad_fibonacci(n-1) + bad_fibonacci(n-2)

cache = {}
def good_fibonacci(n: int)
    if n in cache:
        return cache[n]
    if n <= 1:
        value = n
    else:
        value = good_fibonacci(n - 1) + good_fibonacci(n - 2)
    cache[n] = value
    return value

def exp(a, b):
    if b == 0:
        return 1
    return a * pow(a, b - 1)

def efficient_exp(a, b: int):
    if b < 0:
        return("error: power must be a whole number")
    if b == 0:
        return 1
    elif b % 2 == 1:
        mult = efficient_exp(a, b//2)
        return a * mult * mult
    else:
        mult = efficient_exp(a, b//2)
        return mult * mult

import os
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total

def iterative_binarySearch(data, target):
    low = 0
    high = len(data) - 1
    while low < high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def iterative_reverse(S):
    start = 0
    stop = len(S) - 1
    while start < stop:
        S[start], S[stop] = S[stop], S[start]
        start += 1
        stop -= 1