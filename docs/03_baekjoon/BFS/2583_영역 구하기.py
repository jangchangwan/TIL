
def BFS(sr, sc):
    global visited
    queue = []
    queue.append((sr, sc))
    visited[sr][sc] = 1
    cnt = 1
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 좌표 범위 내  and  색칠한 부위 x  and 방문한 곳 x
            if (0 <= nr < N) and (0 <= nc < M) and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
                rear += 1
    return cnt
        

N, M, TC = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
count = 0
answer = []

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(TC):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            arr[j][i] = 1


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            ans = BFS(i, j)
            answer.append(ans)
            count += 1

answer.sort()

print(count)
print(*answer)
            