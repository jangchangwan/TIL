# 1026_보물_문제풀이
# 2022-04-27

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B를 정렬시키지 않고 해야하므로 실패

# A.sort(reverse=True)
# B.sort()
#
# S = 0
# for i in range(N):
#     S += A[i]*B[i]
#
# print(S)
C = B[:]
A.sort()
res = [0] * N
for i in range(N):
    for j in range(N):
        if C[j] == max(C):
            C[j] = 0
            res[j] = A[i]
            break

S = 0
for i in range(N):
    S += res[i]*B[i]
print(S)