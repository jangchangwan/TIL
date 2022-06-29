# 2638_치즈
# 2022-06-29
# BFS 탐색
# Pypy3 118092 KB / 260 ms
# Python3 32484 KB / 984 ms

from collections import deque
# 외부라는 것을 어떻게 조건을 걸것인가?
'''
모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 
<- 조건이 0,0을 시작점을 잡아라는 의미 인거같다.

치즈를 벽이라고 생각하고 치즈를 만날경우
카운팅만하고 큐에 좌표를 넣어주지 않을 경우
섬 처럼 외부만 탐색하게 된다.
'''


def BFS(sr, sc):
    global visited, arr

    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0:
                # 외부라는 조건
                if arr[nr][nc] >= 1:
                    arr[nr][nc] += 1
                else:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    visited = [[0] * M for _ in range(N)]
    BFS(0, 0)
    flag = 0 # 녹을 치즈가 있는지 없는지 확인
    for i in range(N):
        for j in range(M):
            # 두 변 이상 외부에 노출되어있는 경우
            if arr[i][j] >= 3:
                arr[i][j] = 0 # 빈 공간으로 변환
                flag = 1
            # 한 변만 노출 된경우 다시 치즈로 변환
            elif arr[i][j] == 2:
                arr[i][j] = 1
    # 치즈 유무 확인
    if flag:
        time += 1
    else:
        break

# 출력
print(time)