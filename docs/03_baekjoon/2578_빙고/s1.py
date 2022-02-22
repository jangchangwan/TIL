# 2578_빙고_문제풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

bingo_arr = [list(map(int, input().split())) for _ in range(5)]
num_list = []
for i in range(5):
    num = list(map(int, input().split()))
    num_list += num

cnt = 0
for k in range(25):
    # 빙고일경우 0으로 변환
    for i in range(5):
        for j in range(5):
            if bingo_arr[i][j] == num_list[k]:
                bingo_arr[i][j] = 0
    cnt += 1
    bingo_cnt = 0
    # 3줄 빙고를 위한 최소 갯수
    if cnt > 11:
        # 가로줄 빙고
        for i in range(5):
            row_sum = 0
            for j in range(5):
                row_sum += bingo_arr[i][j]

            if row_sum == 0:
                bingo_cnt += 1
        # 세로줄 빙고
        for j in range(5):
            col_sum = 0
            for i in range(5):
                col_sum += bingo_arr[i][j]
            if col_sum == 0:
                bingo_cnt += 1
        # 대각선 빙고
        cro_sum_1 = 0
        cro_sum_2 = 0
        for i in range(5):
            cro_sum_1 += bingo_arr[i][i]
            cro_sum_2 += bingo_arr[4 - i][i]
        if cro_sum_1 == 0:
            bingo_cnt += 1
        if cro_sum_2 == 0:
            bingo_cnt += 1

    if bingo_cnt >= 3:
        break

print(cnt)