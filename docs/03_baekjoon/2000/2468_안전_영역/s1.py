# 2468_안전_영역_문제풀이
# 2022-03-17

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 찾기
max_height = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_height:
            max_height = arr[i][j]


max_cnt = 0
for h in range(1, max_height-1):
    cnt = 0
    for i in range(N):
        for j in range(N):
            temp_cnt = 0
            max_num = 0
            # 잠긴 높이보다 높은 곳만 실행
            if arr[i][j] > h:
                # 4방향 탐색
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni = i + di
                    nj = j + dj
                    # 범위 벗어나지 않고 인접한 곳중 안잠긴 곳만 실행
                    if (0 <= ni < N) and (0 <= nj < N) and (arr[ni][nj] > h):
                        # 체크
                        temp_cnt += 1
                        # 인접한 곳중에 가낭 큰값
                        if arr[ni][nj] > max_num:
                            max_num = arr[ni][nj]
            # 가장큰값이고 인접한 곳이 있을 경우 체크
            if temp_cnt > 0 and arr[i][j] > max_num:
                cnt += 1
    # 최대값 측정
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)
