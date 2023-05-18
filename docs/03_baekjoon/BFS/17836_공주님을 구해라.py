

# sr, sc : 출발좌표
# er, ec : 도착좌표
def BFS():
    global item
    queue = []
    queue.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        if arr[r][c] == 2:
            item = visited[r][c] + (N-1-r + M-1-c) - 1
        if r == N-1 and c == M-1:
            return min(visited[r][c]-1, item)
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                rear += 1
    return item


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
item = 10001

answer = BFS()

if answer <= T:
    print(answer)
else:
    print("Fail")
