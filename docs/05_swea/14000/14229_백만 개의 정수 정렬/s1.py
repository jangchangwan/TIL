import sys
sys.stdin = open('input.txt', 'r')

def hoare(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)

N_lst = list(map(int, input().split()))
# A = [7, 1, 1, 1, 7]
N = len(N_lst)
qsort(N_lst, 0, N-1)
print(N_lst[500000])