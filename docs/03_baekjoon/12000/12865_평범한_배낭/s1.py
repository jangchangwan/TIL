# 12865_평범한_배낭_문제풀이
# 2022-04-21
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())

backpack = [[0, 0]]
for i in range(1, N + 1):
    backpack.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= backpack[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-backpack[i][0]] + backpack[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])

