import sys
sys.stdin = open('input.txt', 'r')


def DFS(i, j, d):
    global dir_data
    stack = [(i, j, d)]
    visited[i][j] = 1
    cnt = 1
    while stack:
        print(stack)
        r, c, d = stack.pop()
        temp = d
        # 4방향 청소 확인
        clean = True
        for dr, dc in dir_data[d]:
            temp += 3
            nr = r + dr
            nc = c + dc
            if (0 <= nr < row) and (0 <= nc < col) and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                nd = temp % 4
                stack.append((nr, nc, nd))
                cnt += 1
                clean = False
                # 전진 후 빠져나온다
                break
            # 4방향 탐색했을 떄 없을 경우
        if clean:
            nr = r - dir_data[nd][3][0]
            nc = c - dir_data[nd][3][1]
            # 후진 했을 때 벽일경우 중지
            if arr[nc][nr] == 1:
                return cnt
            # 아닐 경우
            else:
                stack.append((nr, nc, nd))


dir_data =[
    # 북 : 서 -> 남 -> 동 -> 북
    [(0, -1), (1, 0), (0, 1), (-1, 0)],
    # 동 : 북 -> 서 -> 남 -> 동
    [(-1, 0), (-1, 0), (1, 0), (0, 1)],
    # 남 : 동 -> 북 -> 서 -> 남
    [(0, 1), (-1, 0), (-1, 0), (1, 0)],
    # 서 : 남 -> 동 -> 북 -> 서
    [(1, 0), (0, 1), (-1, 0), (-1, 0)]
]


row, col = map(int, input().split())
start_r, start_c, start_dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
visited = [[0]*col for _ in range(row)]

ans = DFS(start_r, start_c, start_dir)
print(ans)