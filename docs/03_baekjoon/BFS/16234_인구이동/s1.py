# 16234_인구_이동_문제풀이
# 2022-04-12

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    Q = deque()
    Q.append((i, j))
    temp = []
    temp.append((i, j))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                if L <= abs(arr[x][y] - arr[xx][yy]) <= R:
                    visited[xx][yy] = 1
                    Q.append((xx, yy))
                    temp.append((xx, yy))
    return temp

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, L, R = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    isMoved = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                tmp = BFS(i, j)
                if len(tmp) > 1:
                    isMoved = True
                    num = sum([arr[x][y] for x, y in tmp]) // len(tmp)
                    for x, y in tmp:
                        arr[x][y] = num
    if not isMoved:
        break
    cnt += 1
print(cnt)