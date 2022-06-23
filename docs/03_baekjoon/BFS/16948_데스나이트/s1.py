# 16948_데스나이트
# 2022-06-20

from collections import deque


def BFS(sr, sc):
    global visited
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    while queue:
        r, c = queue.popleft()

        if r == ei and c == ej:
            return visited[r][c] - 1
        for d in range(6):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
    return -1


dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

N = int(input())

arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

si, sj, ei, ej = map(int, input().split())

ans = BFS(si, sj)
print(ans)