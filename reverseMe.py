def reverseMe(A):
    n = len(A)
    B = []*n
    C = []*n
    while len(A) != 0:
        B.append(A.pop())
    while len(B)!= 0:
        C.append(B.pop())
    while len(C) != 0:
        A.append(C.pop())

# A = [1,2,3,4,5]
# reverseMe(A)
# for i in range(len(A)):
#     print(A.pop())