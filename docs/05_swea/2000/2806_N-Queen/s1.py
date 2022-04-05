# 2806_N-Queen_문제풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


def DFS(n):
    global ans
    if n == N:
        ans += 1
        return
    else:
        for i in range(N):
            visited[n] = i
            if check(n):
                DFS(n+1)


# 놓을 수 있는 곳인지 확인
def check(n):
    for i in range(n):
        # 상하, 대각선 검토
        if (visited[i] == visited[n]) or ((n - i) == abs(visited[n] - visited[i])):
            return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = 0
    visited = [0] * N
    DFS(0)
    print('#{} {}'.format(tc, ans))