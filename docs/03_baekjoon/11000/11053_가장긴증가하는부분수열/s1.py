# 11053_가장 긴 증가하는 부분 수열
# 2022-04-27


import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
N_lst = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if N_lst[i] > N_lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))