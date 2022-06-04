# 1245_농장관리_문제풀이
# 2022-06-04

import sys
sys.stdin = open('input.txt', 'r')


def BFS(sr, sc):
    global visited, cnt
    cnt += 1 # 우선 들어왔으니 1 추가
    temp_visited = [[0] * M for _ in range(N)]
    front = -1
    rear = 0
    san_peak = arr[sr][sc]
    queue = [(sr, sc)]
    while front != rear:
        front += 1
        r, c = queue[front]
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and temp_visited[nr][nc] == 0:
                # 산봉우리가 아닌 경우
                if arr[nr][nc] > san_peak:
                    cnt -= 1
                    return False
                # 인접한 산봉우리 찾기
                elif arr[nr][nc] == arr[r][c]:
                    if visited[nr][nc]:
                        cnt -= 1
                        return True
                    temp_visited[nr][nc] = 1
                    queue.append((nr, nc))
                    rear += 1
    return True


# 8방위 탐색
dr = [1, 1, 1, 0, 0, -1, -1, -1]
dc = [1, 0, -1, 1, -1, 1, 0, -1]

# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방문
visited = [[0]*M for _ in range(N)]

# 산봉우리 갯수
cnt = 0

# 탐색시작
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            if BFS(i, j):
                visited[i][j] = 1

# 출력
print(cnt)