# 13301_타일 장식물
# 2022-06-02

N = int(input())

dp = [0] * (N+2)

dp[1] = 1
dp[2] = 1

# 1 1 1 1
# 1 1 2 2
# 2 2 3 3
# 3 3 5 5
# 5 5 8 8
# 8 8 13 13

for n in range(3, N+2):
    dp[n] = dp[n-2] + dp[n-1]

ans = (dp[N]+dp[N+1]) * 2
print(ans)