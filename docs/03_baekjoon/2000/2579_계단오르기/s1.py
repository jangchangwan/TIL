# 2579_계단 오르기_문제풀이
# 2022-05-13

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
N_lst = list(int(input()) for _ in range(N))

if N == 1:
    print(N_lst[0])
else:
    DP = [0, N_lst[0], N_lst[0]+N_lst[1]]

    for i in range(3, N+1):
        DP.append(max(DP[i-3]+N_lst[i-2]+N_lst[i-1], DP[i-2]+N_lst[i-1]))

    print(DP[-1])


