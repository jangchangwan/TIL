# 2206_벽_부수고_이동하기_문제풀이
# 2022-04-05
import sys
sys.stdin = open('input.txt', 'r')


def BFS(r, c, crash):
    q = [(r, c, crash)]
    front = -1
    rear = 0
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while front != rear:
        front += 1
        a, b, w = q[front]
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                    rear += 1
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
                    rear += 1
    return -1


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int,input().split())
s = [list(map(int, input())) for _ in range(n)]
print(BFS(0, 0, 1))