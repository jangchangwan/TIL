# 3187_양치기 꿍
# 2022-06-28
# BFS
from collections import deque


def BFS(sr, sc):
    global sheep, wolf
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    if arr[sr][sc] == 'v':
        wolf += 1
    elif arr[sr][sc] == 'k':
        sheep += 1

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0 and arr[nr][nc] != '#':
                visited[nr][nc] = 1
                queue.append((nr, nc))
                if arr[nr][nc] == 'v':
                    wolf += 1
                elif arr[nr][nc] == 'k':
                    sheep += 1
    return


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = [0, 0]

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] != '#':
            sheep, wolf = 0, 0
            BFS(i, j)
            if sheep > wolf:
                answer[0] += sheep
            else:
                answer[1] += wolf

print(*answer)