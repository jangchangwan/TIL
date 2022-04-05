# 5205_퀵_정렬_문제풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')

# A : 배열, l : 처음, r : 끝
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


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = list(map(int, input().split()))

    qsort(N_arr, 0, N-1)
    ans = N_arr[N//2]
    print('#{} {}'.format(tc, ans))