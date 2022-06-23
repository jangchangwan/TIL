# 1799_비숍_문제풀이
# 2022_06_03

import sys


'''
체스판에서 흰색과 검은색은 비숍인 경우 서로 영향을 주지않는다.
그래서 2가지경우를 나누어 생각헤서 짜본다.
'''


def bishop(coordinates, index, cnt):
    global black_ans, white_ans

    if index == len(coordinates):
        rr, rc = coordinates[index - 1]
        if color[rr][rc]:
            black_ans = max(black_ans, cnt)
        else:
            white_ans = max(white_ans, cnt)
        return

    r, c = coordinates[index]
    if visited_01[r+c] or visited_02[r-c+N-1]:
        bishop(coordinates, index+1, cnt)
    else:
        visited_01[r+c] = 1
        visited_02[r-c+N-1] = 1
        bishop(coordinates, index + 1, cnt + 1)
        visited_01[r + c] = 0
        visited_02[r - c + N - 1] = 0
        bishop(coordinates, index + 1, cnt)



N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]
color = [[0]*N for _ in range(N)]
black = []
white = []
# 대각선 visited 함수
visited_01 = [0] * (N*2-1)
visited_02 = [0] * (N*2-1)
# 체스판 색깔만들기
for i in range(N):
    for j in range(N):
        color[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)

for i in range(N):
    for j in range(N):
        # 놓을수 있는 곳에서 검은색 흰색 찾기
        if arr[i][j]:
            if color[i][j]:
                black.append((i, j))
            else:
                white.append((i, j))

black_ans, white_ans = 0, 0

if len(black) > 0:
    bishop(black, 0, 0)
if len(white) > 0:
    bishop(white, 0, 0)
ans = black_ans + white_ans
print(ans)