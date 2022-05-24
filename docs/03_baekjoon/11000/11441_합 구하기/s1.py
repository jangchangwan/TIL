# 11441_합 구하기_문제풀이
# 2022-05-23

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

N_lst = list(map(int, input().split()))
total = [N_lst[0]]
for i in range(1, N):
    total.append(total[-1] + N_lst[i])

T = int(input())
for tc in range(T):
    start, end = map(int, input().split())
    if start == 1:
        print(total[end - 1])
    else:
        print(total[end - 1] - total[start - 2])