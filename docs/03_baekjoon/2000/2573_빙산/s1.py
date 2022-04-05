# 2573_빙산_문제풀이
# 2022-03-21
import sys
sys.stdin = open('input.txt', 'r')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def ice_melt(i, j):
    queue = [(i, j)]
    visited[i][j] = 1  # 방문 표시
    front = -1
    rear = 0
    while front != rear:
        front += 1
        x, y = queue[front]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if ice[nx][ny] != 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    rear += 1
                elif ice[nx][ny] == 0:  # 주변이 바다라면 +1
                    count[x][y] += 1


# 입력받기
n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
days = 0  # 답 출력

while True:
    count = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    flag = 0
    # 빙산 탐색
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and ice[i][j] != 0:
                flag += 1
                ice_melt(i, j)
    # 모두 탐색했다면
    if flag == 0:
        days = 0
        break
    # 분리 되었는지 확인
    if flag >= 2:
        break
    # 날짜 추가
    days += 1
    # 빙산 녹이기
    for i in range(n):
        for j in range(m):
            ice[i][j] -= count[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
print(days)