# 10026_적록색약_문제풀이
# 2022-06-08

from collections import deque


def BFS(sr, sc, arr):
    global visited
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    color = arr[sr][sc]
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0 and arr[nr][nc] == color:
                visited[nr][nc] = 1
                queue.append((nr, nc))
    return


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 입력
N = int(input())
arr = [list(input()) for _ in range(N)]

# 적록색약인 사람이 봤을때 배열
arr_2 = [['R'] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            arr_2[i][j] = 'B'

answers = [0, 0]
visited = [[0] * N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, arr)
            ans += 1
answers[0] = ans
visited = [[0] * N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, arr_2)
            ans += 1
answers[1] = ans
print(*answers)