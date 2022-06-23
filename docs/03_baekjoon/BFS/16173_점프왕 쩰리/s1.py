# 16173_점프왕 쩰리_문제풀이
# 2022-06-09
from collections import deque


def BFS():
    queue = deque()
    # 시작위치
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        # 도착점에 도달했을 경우
        if arr[r][c] == -1:
            return True
        for d in range(2):
            nr = r + dr[d] * arr[r][c]
            nc = c + dc[d] * arr[r][c]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr, nc))
    # 불가능 한 경우
    return False


dr = [1, 0]
dc = [0, 1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
if BFS():
    print('HaruHaru')
else:
    print('Hing')