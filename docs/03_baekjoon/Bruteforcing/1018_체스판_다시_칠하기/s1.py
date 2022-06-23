# 1018_체스판_다시_칠하기_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')


row, col = map(int, input().split())
chess_arr = [list(input()) for _ in range(row)]

W_cnt = B_cnt = 0
min_ans = 64
for i in range(row-7):
    for j in range(col-7):
        ans = 0
        # 8 x 8 탐색
        # 흰색으로 시작하는 경우

        for r in range(8):
            for c in range(8):
                if r % 2 == 0 and c % 2 == 0 and chess_arr[i + r][j + c] == 'B':
                    ans += 1
                elif r % 2 == 0 and c % 2 == 1 and chess_arr[i + r][j + c] == 'W':
                    ans += 1
                elif r % 2 == 1 and c % 2 == 0 and chess_arr[i + r][j + c] == 'W':
                    ans += 1
                elif r % 2 == 1 and c % 2 == 1 and chess_arr[i + r][j + c] == 'B':
                    ans += 1
        # 검은색으로 시작하는 경우
        min_ans = min(min_ans, ans)
        ans = 0
        for r in range(8):
            for c in range(8):
                if r % 2 == 0 and c % 2 == 0 and chess_arr[i+r][j+c] == 'W':
                    ans += 1
                elif r % 2 == 0 and c % 2 == 1 and chess_arr[i+r][j+c] == 'B':
                    ans += 1
                elif r % 2 == 1 and c % 2 == 0 and chess_arr[i+r][j+c] == 'B':
                    ans += 1
                elif r % 2 == 1 and c % 2 == 1 and chess_arr[i + r][j + c] == 'W':
                    ans += 1

        min_ans = min(min_ans, ans)

print(min_ans)