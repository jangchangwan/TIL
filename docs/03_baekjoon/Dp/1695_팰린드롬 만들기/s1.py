# 1695_팰린드럼 만들기
# 2022-06-25

N = int(input())
N_lst = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if N_lst[-i] == N_lst[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(N-dp[N][N])