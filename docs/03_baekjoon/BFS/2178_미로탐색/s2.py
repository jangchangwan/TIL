import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def dfs(i,j):
    global visited
    stack = [(i,j)]
    while stack:
        i, j = stack.pop()
        for i in range(4):
            ni, nj = i + di[i], j + dj[i]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 1:
                if visited[ni][nj] == 0 or visited[ni][nj] > visited[i][j] + 1:
                    stack.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1



dfs(0,0)
print(visited[n-1][m-1])
print(visited)

