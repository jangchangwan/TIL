# 2748_피보나치 수 2_문제풀이
# 2022-05-13


N = int(input())

dp = [0, 1]


for n in range(2, N+1):
    dp.append(dp[n-2]+dp[n-1])

print(dp[-1])