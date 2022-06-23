# 1987_알파벳_문제풀이
# 2022-06-06
# 시간초과
from collections import deque


def BFS():
    global answer
    queue = deque()
    queue.append((0, 0, arr[0][0]))

    while queue:
        r, c, ans = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < R) and (0 <= nc < C) and (arr[nr][nc] not in ans):
                queue.append((nr, nc, ans + arr[nr][nc]))
                answer = max(answer, len(ans) + 1)


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 입력
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
answer = 1
BFS()
print(answer)
