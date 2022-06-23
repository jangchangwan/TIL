# 9461_파도반 수열_문제풀이
# 2022-05-29

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

DP = [0, 1, 1, 1, 2, 2, 3]
for t in range(T):
    N = int(input())
    if N < len(DP):
        print(DP[N])
    else:
        for n in range(len(DP)-1, N+1):
            DP.append(DP[n]+DP[n-4])
        print(DP[N])