# 1012_유기농 배추 문제풀이
# 2022-03-26

import sys
sys.stdin = open('input.txt', 'r')


def BFS(row, col):
    queue = [(row, col)]
    visited[row][col] = 1
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and (visited[nr][nc] == 0) and (base_arr[nr][nc] == 1):
                visited[nr][nc] = 1
                queue.append((nr, nc))
                rear += 1
    return


T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    base_arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        base_arr[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if base_arr[i][j] == 1 and visited[i][j] == 0:
                BFS(i, j)
                cnt += 1

    print(cnt)