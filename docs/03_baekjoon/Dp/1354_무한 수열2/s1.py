# 1354_무한 수열 2_문제풀이
# 2022-06-04
from collections import defaultdict


def DFS(n):
    if n <= 0:
        return 1
    if dp[n]:
        return dp[n]
    else:
        dp[n] = DFS(n//P - X) + DFS(n//Q - Y)
        return dp[n]


N, P, Q, X, Y = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

DFS(N)
print(dp[N])

