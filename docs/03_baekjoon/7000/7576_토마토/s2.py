# 7576_토마토_문제풀이
# 2022-04-12

'''
전형적인 최소경로를 BFS 문제
방향은 상하좌우
익은 토마토들의 좌표를 탐색하고 queue에 담은다음 탐색하면 될것같다
'''

import sys
sys.stdin = open('input.txt', 'r')


def BFS():
    global queue, cnt
    front = 0
    rear = len(queue)
    while front != rear:
        r, c = queue[front]
        front += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < ROW) and (0 <= nc < COL) and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc))
                rear += 1
                cnt += 1
    return


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

COL, ROW = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(ROW)]

# 익은 사과 담기
cnt = 0
total_cnt = COL * ROW
queue = []
for i in range(ROW):
    for j in range(COL):
        if arr[i][j] == 1:
            queue.append((i, j))
            cnt += 1
        elif arr[i][j] == -1:
            total_cnt -= 1


BFS()
ans = 0
for i in arr:
    for j in i:
        ans = max(ans, j)

if total_cnt != cnt:
    print(-1)
else:
    print(ans - 1)