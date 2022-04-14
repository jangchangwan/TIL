# 2407_조합_문제풀이
# 2022-04-13

import sys
sys.stdin = open('input.txt', 'r')


'''
조합 경우의수는 nCm = n! / ( m! * (m - n ) ! )

'''


N, M = map(int, input().split())

K = N - M

if M > K:
    up = 1
    for i in range(M+1, N+1):
        up *= i
    down = 1
    for j in range(1, K+1):
        down *= j

    res = up // down

else:
    up = 1
    for i in range(K + 1, N + 1):
        up *= i
    down = 1
    for j in range(1, M + 1):
        down *= j

    res = up // down

print(int(res))