# 1806_부분합_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, S = map(int, input().split())
N_lst = list(map(int, input().split()))


start, end, total = 0, 0, 0
min_S = 100001

while start < N:
    if total >= S:
        min_S = min(min_S, end-start)
        total -= N_lst[start]
        start += 1
    elif end == N:
        break
    else:
        total += N_lst[end]
        end += 1
if min_S != 100001:
    print(min_S)
else:
    print(0)
