# 25214_크림 파스타_문제풀이
# 2022-05-26

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
N_lst = list(map(int, input().split()))

DP = [0] * N
min_N = N_lst[0]
for i in range(1, N):
    DP[i] = max(DP[i-1], N_lst[i]-min_N)
    min_N = min(N_lst[i], min_N)

print(*DP)