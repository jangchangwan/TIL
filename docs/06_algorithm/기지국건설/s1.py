import sys
sys.stdin = open('input.txt', 'r')


def DFS(r, c, cnt, total):
    global ans
    if cnt == 4:
        if ans < total:
            ans = total
        return

    else:
        # 아래 대각선
        if (r % 2) == 1 and (c % 2) == 1:
            for dr, dc in [(1, 0), (-1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < H) and (0 <= nc < W) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if cnt == 2:
                        DFS(r, c, cnt + 1, total + arr[nr][nc])
                    DFS(nr, nc, cnt + 1, total + arr[nr][nc])
                    visited[nr][nc] = 0
        # 위 대각선
        elif (r % 2) == 1 and (c % 2) == 0:
            for dr, dc in [(1, 0), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < H) and (0 <= nc < W) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if cnt == 2:
                        DFS(r, c, cnt + 1, total + arr[nr][nc])
                    DFS(nr, nc, cnt + 1, total + arr[nr][nc])
                    visited[nr][nc] = 0
        # 아래 대각선
        elif (r % 2) == 0 and (c % 2) == 1:
            for dr, dc in [(1, 0), (-1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < H) and (0 <= nc < W) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if cnt == 2:
                        DFS(r, c, cnt + 1, total + arr[nr][nc])
                    DFS(nr, nc, cnt + 1, total + arr[nr][nc])
                    visited[nr][nc] = 0
        # 위 대각선
        elif (r % 2) == 0 and (c % 2) == 0:
            for dr, dc in [(1, 0), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < H) and (0 <= nc < W) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if cnt == 2:
                        DFS(r, c, cnt + 1, total + arr[nr][nc])
                    DFS(nr, nc, cnt + 1, total + arr[nr][nc])
                    visited[nr][nc] = 0


T = int(input())

for tc in range(1, T+1):
    # 데이터 입력
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    ans = 0

    for i in range(H):
        for j in range(W):

            visited[i][j] = 1
            DFS(i, j, 1, arr[i][j])
            visited[i][j] = 0
    # 데이터 출력

    print('#{} {}'.format(tc, ans**2))