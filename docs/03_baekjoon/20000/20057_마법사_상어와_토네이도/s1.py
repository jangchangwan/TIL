# 20057_마법사_상어와_토네이도_문제풀이
# 2022-03-15

import sys
sys.stdin = open('input.txt', 'r')


def sand(s_x, s_y, direction):
    for dx, dy, z in direction:
        nx = s_x + dx
        ny = s_y + dy
        # 모래 퍼트리기
        if 0 <= nx < N and 0 <= ny < N:  
            arr[nx][ny] += int(arr[s_x][s_y] * z)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


# 초기 모래 값
begin_sand = 0
for i in range(N):
    for j in range(N):
        begin_sand += arr[i][j]

# 변수 초기화
d = 0 # 방향
size = 1 # 방향 크기
cnt = 0 # 반복횟수
dir_lst = list() # 방향 리스트

# 역 토네이도 이동 경로
while cnt < (N * N - 1):
    for i in range(size):
        if cnt >= (N * N - 1):
            continue
        dir_lst.append(d)
        cnt += 1
    d = (d + 1) % 4
    for i in range(size):
        if cnt >= (N * N - 1):
            continue
        dir_lst.append(d)
        cnt += 1
    size += 1
    d = (d + 1) % 4

# 방향별 모래 비율 위치
left = [                        (-2, -1, 0.02),
                (-1, -2, 0.1), (-1, -1, 0.07), (-1, 0, 0.01),
(0, -3, 0.05),  (0, -2, 0.55), (0, -1, 0),
                (1, -2, 0.1), (1, -1, 0.07), (1, 0, 0.01),
                                (2, -1, 0.02)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

# 1.토네이도 회전 방향(y위치)
dict = {0: left, 1: down, 2: right, 3: up}

# 시작점 (중앙값)
row = col = N // 2

# 탐색 순서 왼쪽 -> 아래 -> 오른쪽 -> 위
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]


for i in dir_lst:
    sand(row, col, dict[i])

    row += dir[i][0]
    col += dir[i][1]

after_sand = 0
for i in range(N):
    for j in range(N):
        after_sand += arr[i][j]

print(begin_sand - after_sand)
