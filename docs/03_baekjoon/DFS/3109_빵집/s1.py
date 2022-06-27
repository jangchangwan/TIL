# 3109_빵집
# 2022-06-27
# DFS

def DFS(r, c):
    # 마지막까지 도착한 경우
    if c == (M-1):
        return True

    for d in range(3):
        nr = r + dr[d]
        nc = c + 1
        if (0 <= nr < N) and arr[nr][nc] == '.' and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if DFS(nr, nc):
                return True
    return False


# 동작
dr = [-1, 0, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0

for i in range(N):
    # 파이프를 설치할 수 있는 경우 탐색 시작
    if arr[i][0] == '.':
        if DFS(i, 0):
            cnt += 1
print(cnt)
