# 1764_듣보잡_문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
N_set, M_set = set(), set()
for _ in range(N):
    N_set.add(input())
for _ in range(M):
    M_set.add(input())
ans_lst = sorted(N_set & M_set)

print(len(ans_lst))
for ans in ans_lst:
    print(ans)
