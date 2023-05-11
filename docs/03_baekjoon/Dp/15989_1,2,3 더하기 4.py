

'''

n = 1   1
n = 2   1 + 1 ( 1+1, 2 )
n = 3   1 + 1 + 1 ( 1+1+1, 1+2, 3)
n = 4   1  ( 1+1+1+1, 1+1+2, 1+3, 2+2)
n = 5   4 ( 1+1+1+1+1, 1+1+1+2, 1+1+3, 2+3)
n = 6   6 ( 1+1+1+1+1+1, 1+1+1+1+2, 1+1+1+3, 1+1+2+2, 1+2+3, 2+2+2, 3+3)
'''


N = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(N):
    n = int(input())
    print(dp[n])




N = int(input())

for _ in range(N):
    n = int(input())
    print(((n+3)**2+3)//12)
