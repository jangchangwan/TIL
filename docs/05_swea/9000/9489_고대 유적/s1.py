import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1,T+1):
    row, col = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]
    max_cnt = 0
    for i in range(row):
        cnt_row = 0
        for j in range(col):
            if arr[i][j] == 1:
                cnt_row += 1
                if cnt_row > max_cnt:
                    max_cnt = cnt_row
            else:
                cnt_row = 0
    for i in range(col):
        cnt_col = 0
        for j in range(row):
            if arr[j][i] == 1:
                cnt_col += 1
                if cnt_col > max_cnt:
                    max_cnt = cnt_col
            else:
                cnt_col = 0

    print('#{} {}'.format(t, max_cnt))