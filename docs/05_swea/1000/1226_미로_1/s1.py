# 1226_미로_1_문제풀이
# 2022-03-16
import sys
sys.stdin = open('input.txt', 'r')


def BFS(row, col):
    queue = [(row, col)]
    visited[row][col] = 1
    rear = 0
    front = -1
    while rear != front:
        front += 1
        i, j = queue[front]
        if arr[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 범위를 벗어나지 않고 벽이 아니고 방문하지 않았을 경우 동작
            if arr[ni][nj] == 0 or arr[ni][nj] == 3:
                if visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                    rear += 1
    return 0


T = 10

for tc in range(1, T+1):
    _ = input()
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    ans = BFS(1, 1)
    print("#{} {}".format(tc, ans))