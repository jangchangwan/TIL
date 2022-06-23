# 16395_파스칼의삼각형
# 2022-06-12


N, K = map(int, input().split())
dp = [[] for _ in range(31)]

dp[1] = [1]
dp[2] = [1, 1]


for n in range(3, N+1):
    temp = [1]
    for k in range(0, n-2):
        temp.append(dp[n-1][k]+dp[n-1][k+1])
    temp.append(1)
    dp[n] = temp
print(dp[N][K-1])