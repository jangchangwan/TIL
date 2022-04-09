# 14190_민코씨의 꽃밭_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt')


def BFS(sr, sc):
    global visited, ans
    front = -1
    rear = 0
    queue = [(sr, sc)]
    visited[sr][sc] = 1
    flowers = [arr[sr][sc]]

    while front != rear:
        cnt = 0

        for flower in flowers:
            if flower != 0:
                cnt += flower
        for i in range(len(flowers)):
            if flowers[i] > 0:
                flowers[i] = flowers[i] - 1
        ans.append(cnt)
        front += 1
        r, c = queue[front]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                flowers.append(arr[nr][nc])
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
    ans = []
    BFS(start_r, start_c)

    print(ans)
    cnt = max(ans)
    day = 0
    for a in range(len(ans)-1, -1, -1):

        if ans[a] == cnt:
            day = a + 1
            break


    print('#{} {}일 {}개'.format(tc, day, cnt))