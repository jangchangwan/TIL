# 25307_시루의 백화점 구경
# 2022-06-25
# BFS

from collections import deque


def BFS(sr, sc):
    visited = [[0]*M for _ in range(N)]
    visited[sr][sc] = 1
    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        if (r, c) in chair:
            return visited[r][c] - 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0 and (board[nr][nc] == 0 or board[nr][nc] == 2):
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    # 못찾을 경우
    return -1


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

chair = []
mannequin = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 4:
            sr, sc = i, j
        elif board[i][j] == 3:
            mannequin.append((i, j))
        elif board[i][j] == 2:
            chair.append((i, j))

# 의자가 없는 경우
if chair == []:
    print(-1)
    exit()

queue = deque()
for i, j in mannequin:
    queue.append((i, j, 0))
    board[i][j] = 1

while queue:
    rr, cc, k = queue.popleft()

    for d in range(4):
        nrr = rr + dr[d]
        ncc = cc + dc[d]
        if (0 <= nrr < N) and (0 <= ncc < M) and (board[nrr][ncc] == 0 or board[nrr][ncc] == 2) and k < K:
            board[nrr][ncc] = 1
            queue.append((nrr, ncc, k+1))


ans = BFS(sr, sc)
print(ans)