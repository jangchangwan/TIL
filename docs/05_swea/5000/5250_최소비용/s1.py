# 5250_최소비용_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')


def BFS(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    while front != rear:
        front += 1
        r, c = queue[front]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N):

                # 높은곳으로 이동할 경우
                if arr[nr][nc] > arr[r][c]:
                    fuel = w_arr[r][c] + 1 + (arr[nr][nc] - arr[r][c])
                else:
                    fuel = w_arr[r][c] + 1
                # 최소값
                if w_arr[nr][nc] > fuel:
                    w_arr[nr][nc] = fuel
                    queue.append((nr, nc))
                    rear += 1

    return w_arr[N-1][N-1]


T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 100000000
    w_arr = [[INF] * N for _ in range(N)]
    w_arr[0][0] = 0
    ans = BFS(0, 0)

    print('#{} {}'.format(tc, ans))


