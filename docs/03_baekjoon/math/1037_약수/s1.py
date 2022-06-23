# 1037_약속_문제풀이
# 2022-04-22

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
N_lst = list(map(int, input().split()))

N_lst.sort()

ans = N_lst[0] * N_lst[-1]

print(ans)