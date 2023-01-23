def findDuplicate(B):
    n = len(B)
    for i in range(n):
        x = B[i] % n
        B[i] = B[i] + n
    for i in range(n):
        if B[i] >= 2*n:
            return i