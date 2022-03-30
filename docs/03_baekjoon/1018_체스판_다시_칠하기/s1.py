import sys
sys.stdin = open('input.txt', 'r')

row, col = map(int, input().split())
chess_arr = [list(input()) for _ in range(row)]

W_cnt = B_cnt = 0

for i in range(row):
    for j in range(col):
        if chess_arr[i][j] == 'W':
            W_cnt += 1
        else:
            B_cnt += 1

# 둘중에 높은거 찾기
if W_cnt >= B_cnt:
    max_cnt = W_cnt
    min_cnt = B_cnt
else:
    max_cnt = B_cnt
    min_cnt = W_cnt

total = row * col
cnt = 0
if total % 2 == 0:
    while (max_cnt-min_cnt) !=0:
        max_cnt -= 1
        min_cnt += 1
        cnt += 1
else:
    while (max_cnt-min_cnt) <= 1:
        max_cnt -= 1
        min_cnt += 1
        cnt += 1

print(cnt)