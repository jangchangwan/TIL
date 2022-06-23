# 2156_포도주 시식_문제풀이
# 2022-05-10
# 인덱스 에러 발생
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
N_lst = [int(input()) for _ in range(N)]

dp = [0, N_lst[0], N_lst[0] + N_lst[1]]

for i in range(3, N+1):
    # 3가지 경우
    dp.append(max(dp[i-1], dp[i-2] + N_lst[i-1], dp[i-3] + N_lst[i-1] + N_lst[i-2]))

print(dp[-1])