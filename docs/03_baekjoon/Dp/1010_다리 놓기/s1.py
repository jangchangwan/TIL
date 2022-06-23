# 1010_다리놓기
# 2022-05-14
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


'''
    1   2   3   4   5   6   7
1   1   2   3   4   5   6   7
2   x   1   3   6   10  15  21
3   x   x   1   4   10  20  35
4   x   x   x   1   5   15  35
5   x   x   x   x   1   6   21
6   x   x   x   x   x   1   7
7   x   x   x   x   x   x   1

dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
'''


# 미리 구해놓기
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    dp[i][i] = 1
    dp[1][i] = i

for i in range(30):
    for j in range(30):
        if i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])

