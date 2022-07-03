# 14923_미로 탈출
# 2022-07-04

# 라이브러리
from collections import deque


# 탐색
def BFS(sr, sc):
    visited = [[[0, 0] for j in range(M)] for i in range(N)]
    queue = deque()
    queue.append((0, sr, sc))
    while queue:
        cnt, r, c = queue.popleft()
        if (r == end_row - 1) and (c == end_col - 1):
            return visited[r][c][cnt]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc][cnt] == 0:
                if arr[nr][nc] == 0:
                    queue.append((cnt, nr, nc))
                    visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                elif cnt == 0:
                    visited[nr][nc][1] = visited[r][c][cnt] + 1
                    queue.append((1, nr, nc))
    return -1


# 탐색 방향
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 입력
N, M = map(int, input().split())
start_row, start_col = map(int, input().split())
end_row, end_col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = BFS(start_row-1, start_col-1)
print(answer)