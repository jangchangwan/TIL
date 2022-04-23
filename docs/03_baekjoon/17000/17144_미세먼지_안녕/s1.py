# 17144 미세먼지 안녕! 문제풀이
# 2022-04-23
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

'''
1. 확산
    1) 네방향
    2) 범위 벗어나거나 공기청정기가 있을경우 동작 x
    3) 크기를 K라고했을때 K//5
    4) 확산되고 남은양 K- (K//5) * (확산된 방향수)
    
2. 제거 & 확산
    1) 위쪽 반시계 방향 확산, 아래쪽 시계방향 확산
    2) 모두 한 칸씩 이동
    3) 공기청정기안으로 들어간 미세먼지는 0이된다.
'''


# 확산
def my_diff():
    temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                cnt = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if (0 <= nr < R) and (0 <= nc < C) and arr[nr][nc] != -1:
                        temp[nr][nc] += arr[r][c] // 5
                        cnt += 1
                temp[r][c] += arr[r][c] - (arr[r][c] // 5) * cnt

    return temp


def cleaner():
    up = air_cleaner[0]
    down = air_cleaner[1]

    # 공기청소기 위 작동
    for i in range(up[0]-1, 0, -1):
        arr[i][up[1]] = arr[i-1][up[1]]
    for i in range(up[1], C-1):
        arr[0][i] = arr[0][i+1]
    for i in range(up[0]):
        arr[i][C-1] = arr[i+1][C-1]
    for i in range(C - 1, up[1], -1):
        arr[up[0]][i] = arr[up[0]][i - 1]
    # 공기청소기 아래 작동
    for i in range(down[0] + 1, R - 1):
        arr[i][down[1]] = arr[i + 1][down[1]]
    for i in range(down[1], C - 1):
        arr[R - 1][i] = arr[R - 1][i + 1]
    for i in range(R - 1, down[0], -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    for i in range(C - 1, down[1], -1):
        arr[down[0]][i] = arr[down[0]][i - 1]

    arr[up[0]][up[1]] = -1
    arr[down[0]][down[1]] = -1
    arr[up[0]][up[1] + 1] = 0
    arr[down[0]][down[1] + 1] = 0

    return


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치
air_cleaner = []
for i in range(R):
    if arr[i][0] == -1:
        air_cleaner.append((i, 0))


# 청소 시작
for i in range(T):
    arr = my_diff()
    cleaner()

ans = 0
for i in range(R):
    ans += sum(arr[i])

print(ans+2)