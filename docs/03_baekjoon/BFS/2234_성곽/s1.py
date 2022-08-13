# 2234_성곽
# 2022-08-13

# python3 32524 KB / 3940 ms
from collections import deque


def BFS(sr, sc):
    global visited
    queue = deque()
    queue.append([sr, sc])
    visited[sr][sc] = 1
    cnt = 1
    while queue:
        r, c = queue.popleft()
        wall = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < M) and (0 <= nc < N) and visited[nr][nc] == 0 and (arr[r][c] & wall != wall):
                cnt += 1
                visited[nr][nc] = 1
                queue.append([nr, nc])
            wall = wall * 2
    return cnt


# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
# 변수 설정
visited = [[0] * N for _ in range(M)]
count = 0
max_value = 0
max_value_2 = 0
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 탐색
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            count += 1
            max_value = max(max_value, BFS(i, j))


for i in range(M):
    for j in range(N):
        num = 1
        while num < 9:
            if num & arr[i][j]:
                visited = [[0] * N for _ in range(M)]
                arr[i][j] -= num
                max_value_2 = max(max_value_2, BFS(i, j))
                arr[i][j] += num
            num *= 2

print(count)
print(max_value)
print(max_value_2)
