import sys
sys.stdin = open('input.txt', 'r')


def bfs(arr, i, j, N, M):
    queue = list()             # 큐 생성
    queue.append((i, j))      # 시작점 인큐

    visited[i][j] = 1    # 시작점 방문 표시
    cnt = 1
    # 큐가 비워있지 않으면 반복
    while queue:
        i, j = queue.pop(0)
        if i == N-1 and j == M-1:
            return visited[N-1][M-1] # 출발 도착 칸 제외
        # i, j 에 인접한 칸에 대해서
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            # 범위를 벗어나지 않고 벽이 아니고 방문하지 않았을 경우 동작
            if (0 <= ni < N) and (0 <= nj < M) and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    # 도착지를 찾지 못했을 경우
    return 0


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dirs = [     (-1, 0),
      (0, -1),     (0, 1),
            (1, 0)]
ans = bfs(arr, 0, 0, N, M)
print(ans)