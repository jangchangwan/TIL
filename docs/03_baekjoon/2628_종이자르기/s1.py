# 2628_종이자르기_문제풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')


def my_sort(num):
    for i in range(len(num)-1):
        min_idx = i
        for j in range(i+1, len(num)):
            if num[j] < num[min_idx]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]


def my_diff(arr):
    max_diff = 0
    for i in range(len(arr) - 1):
        now_diff = arr[i + 1] - arr[i]
        if now_diff > max_diff:
            max_diff = now_diff
    return max_diff


col, row = map(int, input().split())
T = int(input())
# 색종이 만들기

row_list = [0, row]
col_list = [0, col]

for t in range(T):
    mode, location = map(int, input().split())

    if mode == 0:
        row_list.append(location)
    else:
        col_list.append(location)

# 정렬
my_sort(row_list)
my_sort(col_list)

# 차이 최대치
max_row = my_diff(row_list)
max_col = my_diff(col_list)

print(max_row*max_col)

