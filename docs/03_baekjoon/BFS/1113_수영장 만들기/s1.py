# 1113_수영장 만들기
# 2022-07-22
# pypy3 117100 kb / 180 ms
from collections import deque


def BFS(sr, sc, h):
    global visited

    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    # 수영장이 아닐 경우
    flag = True
    cnt = 1
    while queue:
        r, c = queue.popleft()

        if r == 0 or r == N-1 or c == 0 or c == M-1:
            flag = False
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if (0 <= nr < N) and (0 <= nc < M):
                if arr[nr][nc] <= h and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    cnt += 1
    if flag:
        return cnt
    return 0


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
answer = 0

for h in range(1, 9):
    visited = [[0] * M for _ in range(N)]
    temp = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] <= h and visited[i][j] == 0:
                temp += int(BFS(i, j, h))
    answer += temp
print(answer)