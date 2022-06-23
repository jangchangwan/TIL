# 14495_피보나치 비스무리한 수열
# 2022-06-20

N = int(input())

dp = [0] * 117

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1

for n in range(4, N+1):
    dp[n] = dp[n-1] + dp[n-3]
print(dp[N])