

# BFS
def BFS():
    global arr

    queue = list()
    cheeze = list()
    queue.append([0, 0])
    front = -1
    rear = 0

    while front != rear:
        front += 1
        r, c = queue[front]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc]:
                visited[nr][nc] = 1
                if arr[nr][nc] == 1: # 치즈인 경우
                    cheeze.append([nr, nc])
                elif arr[nr][nc] == 0: # 공기인 경우
                    queue.append([nr, nc])
                    rear += 1
    
    # 치즈 녹이기
    for i, j in cheeze:
        arr[i][j] = 0
    
    return len(cheeze)

# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

time = 0 # 다 녹는데 걸리는 시간
cnt = 0 # 치즈갯수
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1


# 동작
while True:
    visited = [[0]*M for _ in range(N)]
    delcnt = BFS()
    time += 1
    cnt -= delcnt 
    if cnt <= 0:  # 치즈를 다 녹였으면
        break

# 출력
print(time)
print(delcnt)