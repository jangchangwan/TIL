# 연구소 3
# 2022-06-28
# BFS + 조합
from itertools import combinations
from collections import deque


def BFS(virus_list):
    global visited
    queue = deque()
    cnt = 0
    for sr, sc in virus_list:
        visited[sr][sc] = 1
        queue.append((sr, sc))
        cnt += 1
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and (visited[nr][nc] == 0) and arr[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
                cnt += 1
    return cnt


# 탐색 방향
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 987654321
virus = []
blank = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([i, j])
        if arr[i][j] != 1:
            blank += 1

virus_combination = list(combinations(virus, M))

for v in virus_combination:
    visited = [[0] * N for _ in range(N)]
    cnt = BFS(v)
    if blank == cnt:
        time = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 1 and [i, j] not in virus:
                    time = max(time, visited[i][j])
        answer = min(answer, time-1)

if answer == 987654321:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer)