N = int(input())

visited = [1, 1] + [0] * (N-1)
dp = []

# 소수 구하기 (에라토스테네스의 체)
for i in range(2, N+1):
    if not visited[i]:
        dp.append(i)
        for j in range(2*i, N+1, i):
            visited[j] = True

# 투 포인트
cnt = 0
start = 0
end = 0
while end <= len(dp):
    temp_sum = sum(dp[start:end])
    if temp_sum == N:
        cnt += 1
        end += 1
    elif temp_sum < N:
        end += 1
    else:
        start += 1

print(cnt)