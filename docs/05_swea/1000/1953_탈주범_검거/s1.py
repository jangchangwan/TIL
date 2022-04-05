# 1953_탈주범_검거_문제풀이
# 2022-03-16
import sys
sys.stdin = open('input.txt', 'r')


# 방향 찾기
def dir_pipe(r, c):
    # 상 하 좌 우
    if arr[r][c] == 1:
        return [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 상 하
    elif arr[r][c] == 2:
        return [(-1, 0), (1, 0)]
    # 좌 우
    elif arr[r][c] == 3:
        return [(0, -1), (0, 1)]
    # 상 우
    elif arr[r][c] == 4:
        return [(-1, 0), (0, 1)]
    # 하 우
    elif arr[r][c] == 5:
        return [(1, 0), (0, 1)]
    # 하 좌
    elif arr[r][c] == 6:
        return [(1, 0), (0, -1)]
    # 상 좌
    elif arr[r][c] == 7:
        return [(-1, 0), (0, -1)]
    else:
        return []


# 총 갯수찾기
def BFS(i, j, time):
    queue = [(i, j)]
    front = -1
    rear = 0

    visited[i][j] = 1   # 방문 체크
    while front != rear:
        front += 1
        r, c = queue[front]
        dir = dir_pipe(r, c)
        if visited[r][c] == time:
            return
        # 현재파이프에서 갈수있는 곳으로 가기
        for dr, dc in dir:
            rr = r + dr
            rc = c + dc
            if (0 <= rr < row) and (0 <= rc < col) and arr[rr][rc] != 0 and visited[rr][rc] == 0:
                # 되돌아 갈 수있는지 체크
                dir_r = dir_pipe(rr, rc)
                for drr, drc in dir_r:
                    rrr = rr + drr
                    rcc = rc + drc
                    if (0 <= rrr < row) and (0 <= rcc < col) and (rrr == r) and (rcc == c):
                        queue.append((rr, rc))
                        visited[rr][rc] = visited[r][c] + 1
                        rear += 1


T = int(input())

for tc in range(1, T+1):
    row, col, i, j, time = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0]*col for _ in range(row)]
    BFS(i, j, time)
    ans = 0
    # 시간내에 체크된 파이프 개수 체크하기
    for i in range(row):
        for j in range(col):
            if visited[i][j] != 0 and visited[i][j] <= time:
                ans += 1
    print('#{} {}'.format(tc, ans))