import sys
sys.stdin = open('input.txt', 'r')

# 최소거리 구하기
def BFS(r,c):
    front = -1
    rear = 0
    visited[r][c] = 1
    queue = [(r, c)]
    while front != rear:
        front += 1
        r, c = queue[front]
        # 도착점도 도달시
        if r == N-1 and c == M-1:
            return visited[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                queue.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
                rear += 1

    # 값을 찾지 못한경우
    return -1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int,input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# 시작, 벽 찾기
one_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            one_lst.append((i,j))

min_ans = 1000 * 1000
ans = BFS(0, 0)
if ans != -1:
    min_ans = min(min_ans, ans)
for i in range(len(one_lst)):
    visited = [[0] * N for _ in range(N)]
    r_1, c_1 = one_lst[i]
    arr[r_1][c_1] = 0
    ans = BFS(0, 0)
    if ans != -1:
        min_ans = min(ans, min_ans)
    arr[r_1][c_1] = 1

if min_ans == 1000*1000:
    min_ans = -1
print(min_ans)