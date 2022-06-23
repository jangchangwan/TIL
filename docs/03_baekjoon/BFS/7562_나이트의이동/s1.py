# 7562_나이트의 이동_문제풀이
# 2022-04-24

import sys
sys.stdin = open('input.txt', 'r')


def BFS():
    front = -1
    rear = 0
    queue = [(sr, sc)]
    arr[sr][sc] = 1
    while front != rear:
        front += 1
        r, c = queue[front]
        if r == er and c == ec:
            return arr[r][c] - 1
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc))
                rear += 1
    return


dr = [1, 1, 2, 2, -1, -1, -2, -2]
dc = [2, -2, 1, -1, 2, -2, 1, -1]
T = int(input())

for _ in range(T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    ans = BFS()
    print(ans)