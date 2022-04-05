# 5188_최소합_문제풀이
# 2022-03-29

import sys
sys.stdin = open('input.txt', 'r')


def DFS(r, c, s):
    global ans
    # 초과할경우 더이상 탐색 x
    if s >= ans:
        return
    # 성립할경우 최소값
    if r == (N - 1) and c == (N - 1):
        ans = min(ans, s)
    else:
        for d in range(2):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and (visited[nr][nc] == 0):
                visited[nr][nc] = 1
                DFS(nr, nc, s + N_arr[nr][nc])
                visited[nr][nc] = 0


dr = [1, 0]
dc = [0, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 10 * 13 * 13
    DFS(0, 0, N_arr[0][0])

    print('#{} {}'.format(tc, ans))