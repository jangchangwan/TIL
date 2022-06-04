# 1351_무한 수열_문제풀이
# 2022-06-04
# 메모리초과

import sys
sys.stdin = open('input.txt', 'r')
from collections import defaultdict
'''
N 의 범위가 10^12이여서 그크기의 리스트를 만들경우 메모리 초과가 발생한다
'''


def DFS(n):
    global dp
    if dp[n]:
        return dp[n]
    else:
        dp[n] = DFS(n // P) + DFS(n // Q)
        return dp[n]


# 입력
N, P, Q = map(int, input().split())

# 리스트로 미리 만들고 하는 경우 에러발생
# dp = [0] * (N+1)
# 딕셔너리 형태로 바꾸어서 만들기
dp = defaultdict(int)
dp[0] = 1

# 탐색
DFS(N)

# 출력
print(dp[N])