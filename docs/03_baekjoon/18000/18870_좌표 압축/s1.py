# 18870 좌표 압축_문제풀이
# 2022-05-02

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
N_lst = list(map(int, input().split()))

res_lst = sorted(list(set(N_lst)))

dict = {}
for i in range(len(res_lst)):
    dict[res_lst[i]] = i

for n in N_lst:
    print(dict[n], end=' ')