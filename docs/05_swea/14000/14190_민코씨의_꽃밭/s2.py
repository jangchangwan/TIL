# 14190_민코씨의 꽃밭_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt')


def BFS(sr, sc, sw):
    global visited, flower
    front = -1
    rear = 0
    queue = [(sr, sc, sw)]
    visited[sr][sc] = 1

    while front != rear:
        front += 1
        r, c, w = queue[front]
        flower[w] += 1
        flower[w + arr[r][c]] -= 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                queue.append((nr, nc, w + 1))
                visited[nr][nc] = 1
                rear += 1

    return


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int , input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start_r, start_c = map(int, input().split())
    visited = [[0] * M for _ in range(N)]
    flower = [0 for _ in range(1250001)]
    ans = []
    BFS(start_r, start_c, 1)

    now_cnt = 0
    max_cnt = -1
    max_day = -1
    for day in range(1, 1250001):
        now_cnt += flower[day]
        if max_cnt < now_cnt:
            max_cnt = now_cnt
            max_day = day

    print('#{} {}일 {}개'.format(tc, max_day, max_cnt))