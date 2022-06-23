import sys
sys.stdin = open('input.txt', 'r')

N = int(input())


data_lst = list()

max_row = max_col = 0
for i in range(6):
    # 데이터 받아오기
    new_dir, new_dis = map(int, input().split())
    data_lst.append((new_dir, new_dis))
    # 최대 가로 세로 길이 구하기
    if data_lst[i][0] == 1 or data_lst[i][0] == 2:
        if data_lst[i][1] > max_col:
            max_col = data_lst[i][1]
            max_col_idx = i
    elif data_lst[i][0] == 3 or data_lst[i][0] == 4:
        if data_lst[i][1] > max_row:
            max_row = data_lst[i][1]
            max_row_idx = i


min_row = abs(data_lst[(max_row_idx+1) % 6][1] - data_lst[(max_row_idx-1) % 6][1])
min_col = abs(data_lst[(max_col_idx+1) % 6][1] - data_lst[(max_col_idx-1) % 6][1])


ans = ((max_row * max_col) - (min_row * min_col)) * N
print(ans)