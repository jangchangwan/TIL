# 11650_좌표 정렬하기_문제풀이
# 2022-04-06

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

N_lst = []
for _ in range(N):
    r, c = map(int, input().split())
    N_lst.append((r, c))

N_lst.sort()
for n in N_lst:
    print(n[0], n[1])
