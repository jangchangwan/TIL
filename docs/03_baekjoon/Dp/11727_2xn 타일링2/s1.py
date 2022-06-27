# 11727_2xn 타일링 2
# 2022-06-27
# Dp
N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
  dp[i] = dp[i - 2] * 2 + dp[i - 1]

print(dp[N] % 10007)