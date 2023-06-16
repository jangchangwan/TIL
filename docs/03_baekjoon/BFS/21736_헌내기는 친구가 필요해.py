"""
도연이는 상하좌우로 이동가능 / 범위밖으로는 이동불가능

"""
def FIND_START(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "I":
                return i, j

def BFS(sr, sc):
    global visited
    queue = list()
    queue.append([sr, sc])
    visited[sr][sc] = 1
    count = 0
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        
        if campus[r][c] == "P":
            count += 1
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc] and campus[nr][nc] != "X":
                rear += 1
                visited[nr][nc] = 1
                queue.append([nr, nc])
    return count

N, M = map(int, input().split())

campus = [list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

sr, sc = FIND_START(campus)
answer = BFS(sr, sc)
if answer:
  print(answer)
else:
  print('TT')