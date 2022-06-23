# 1788_피보나치 수의 확장
# 2022-06-20

N = int(input())

if N % 2 == 0 and N < 0:
    print(-1)
    N = abs(N)
elif N == 0:
    print(0)
else:
    print(1)
    N = abs(N)

dp = [0, 1]

for i in range(2, N+1):
    dp.append((dp[i-1] + dp[i-2]) % 1000000000)

print(dp[N])