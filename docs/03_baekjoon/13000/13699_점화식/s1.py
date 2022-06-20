# 13699_점화식
# 2022-06-20

N = int(input())
dp = [0] * 36
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    temp = 0
    if i % 2:
        for j in range(i // 2):
            temp += 2 * dp[j] * dp[i - j - 1]
        dp[i] = temp + dp[i // 2] ** 2
    else:
        for j in range(i // 2):
            temp += 2 * dp[j] * dp[i - j - 1]
        dp[i] = temp
print(dp[N])