# 15624_피보나치 7
# 2022-06-20

N = int(input())
dp = [0] * (N+2)
dp[1] = 1

for n in range(2, N+1):
    dp[n] = (dp[n-1] + dp[n-2]) % 1000000007

print(dp[N])