import collections, sys

sys.stdin = open('input.txt', 'r')

def BFS():
    global curMax
    check = [[-1] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = collections.deque()

    # 바이러스를 모두 돌아주기 위해서 큐에 모든 바이러스를 넣어줌
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 2:
                queue.append((x, y))
                check[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 퍼질수 있는곳 이고(0인곳), 한번도 바이러스가 방문하지 않은 곳이면, 큐에 담는다.
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and check[nx][ny] == -1:
                    queue.append((nx, ny))
                    check[nx][ny] = 0

    # 바이러스가 다 퍼진 다음에 안전영역을 체크하여 count를 세준다.
    count = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0 and check[x][y] == -1:
                count += 1

    curMax = max(curMax, count)


# 3개의 벽을 세우는 모든 경우의 수
def recursive(index):
    # 탈출조건
    if index == 3:
        BFS()
        return

    for x in range(n):
        for y in range(m):
            # 일반구역이라면, 벽을 세워서 다음으로 넘긴다.
            if graph[x][y] == 0:
                graph[x][y] = 1
                recursive(index + 1)
                # 재귀가 끝나면 최대로 3개의 벽을 세울수 있어서 다른곳도 세워보기 위해서 벽을 허문다. 
                graph[x][y] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
curMax = 0

recursive(0)
print(curMax)