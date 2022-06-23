# 2468_안전_영역_문제풀이
# 2022-03-17

import sys
sys.stdin = open('input.txt', 'r')


def BFS(i, j, h):
    global visited
    queue = [(i, j)]
    front = -1
    rear = 0
    visited[i][j] = 1
    while front != rear:
        front += 1
        r, c = queue[front]
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc] > h and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr, nc))
                rear += 1


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 찾기
max_height = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_height:
            max_height = arr[i][j]

max_cnt = 0
for h in range(max_height):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 방문하지않고 안잠긴곳만 동작
            if arr[i][j] > h and visited[i][j] == 0:
                BFS(i, j, h)
                cnt += 1

    # 최대값 측정
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)
