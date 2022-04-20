# 1520_내리막길_문제풀이
# 2022-04-20

import sys
sys.stdin = open('input.txt', 'r')


'''

넓이 우선탐색으로 0,0에서 시작해서 N,M 좌표로 갈수 있을경우 
cnt 1씩 늘린후
cnt 를 출력한다.
메모리초과 발생 front -rear 로 했을때 리스트 메모리가 많아져서 그런거같다

deque를 사용해서 메모리를 줄였다
시간초과 발생 
BFS가 아닌 DPS로 풀어보자
'''
from collections import deque


def BFS():
    global cnt
    queue = deque()
    queue.append((0, 0))
    while queue:
        r, c = queue.popleft()
        if r == (N-1) and c == (M-1):
            cnt += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and arr[r][c] > arr[nr][nc]:
                queue.append((nr, nc))
    return


def DFS(r, c):

    if r == N-1 and c == M-1:
        return 1
    if visited[r][c] == -1:
        visited[r][c] = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if (0 <= nr < N) and (0 <= nc < M) and arr[r][c] > arr[nr][nc]:
                visited[r][c] += DFS(nr, nc)

    return visited[r][c]


input = sys.stdin.readline
# 4 방향
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 행, 열
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

ans = DFS(0, 0)
print(ans)