# 1249_보급로_문제풀이
# 2022-03-29

import sys
sys.stdin = open('input.txt', 'r')


def BFS(sr, sc):
    queue = [(sr, sc)]
    visited[sr][sc] = N_arr[sr][sc]
    front = -1
    rear = 0

    while front != rear:
        front += 1
        r, c = queue[front]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] > (visited[r][c] + N_arr[nr][nc]):
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + N_arr[nr][nc]
                rear += 1
    return visited[N-1][N-1]


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = [list(map(int, input())) for _ in range(N)]
    visited = [[9999] * N for _ in range(N)]
    ans = BFS(0, 0)
    print('#{} {}'.format(tc, ans))




