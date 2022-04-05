# 7569_토마토_문제풀이
# 2022-03-21

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


def bfs():
    while queue:
        row, col, height = queue.popleft()
        visit[row][col][height] = 1
        for i in range(6):
            nr = row + dx[i]
            nc = col + dy[i]
            nh = height + dz[i]

            if (0 <= nr < N) and (0 <= nc < M) and (0 <= nh < H) and (arr[nr][nc][nh] == 0) and (visit[nr][nc][nh] == 0):
                queue.append([nh, nr, nc])
                arr[nh][nr][nc] = arr[row][col][height] + 1
                visit[nh][nr][nc] = 1


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for j in range(N)] for z in range(H)]

visit = [[[0 for i in range(M)] for j in range(N)] for _ in range(H)]


queue = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                queue.append([i, j, h])
bfs()
ans = -1
z = 1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                z = 0
            ans = max(ans, arr[h][i][j])
if z == 0:
    print(-1)
else:
    print(ans - 1)