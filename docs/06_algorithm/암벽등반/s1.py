import sys
sys.stdin = open('input.txt', 'r')


def BFS(sr, sc, dis):
    global temp, visited
    front = -1
    rear = 0
    queue = [(sr, sc)]
    visited[sr][sc] = 1
    while front != rear:
        front += 1
        r, c = queue[front]

        if arr[r][c] == 3:
            return 1

        for d in range(1, dis+1):
            for dr, dc in [(d, 0), (-d, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0:
                    if arr[nr][nc] == 1 or arr[nr][nc] == 3:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
                        rear += 1
    return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    start = []
    end = []

    ans = 0
    for distance in range(1, N):
        visited = [[0] * M for _ in range(N)]
        temp = BFS(N-1, 0, distance)
        if temp == 1:
            ans = distance
            break

    print('#{} {}'.format(tc, ans))