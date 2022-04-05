# 14195_미생물_관찰_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')

def BFS(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    visited[sr][sc] = 1
    cnt = 1
    while front != rear:
        front += 1
        r, c = queue[front]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0 and arr[nr][nc] == arr[r][c]:
                visited[nr][nc] = 1
                queue.append((nr, nc))
                rear += 1
                cnt += 1
    return cnt

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    A_lst = []
    B_lst = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                if arr[i][j] == 'A':
                    A_lst.append(BFS(i, j))
                elif arr[i][j] == 'B':
                    B_lst.append(BFS(i, j))

    print('#{} {} {} {}'.format(tc, len(A_lst), len(B_lst), max(A_lst+B_lst)))
