"""
Trailing zero 라는 것은 결국 
소인수 2, 5 의 갯수를 말하는 것

"""

T = int(input())
INF = 987654321
for tc in range(T):
    N, K = map(int, input().split())
    stones = list(map(int, input().split()))
    
    dp = [[0] * (2) for _ in range(N)]
    
    for i in range(N):

        if i:
            dp[i][0], dp[i][1] = INF, INF
        for j in range(1, K+1):
            if (i - j) < 0:
                break
            
            dp[i][0] = min(dp[i][0], dp[i-j][0])
            dp[i][1] = min(dp[i][1], dp[i-j][1])

        while stones[i] % 2 == 0:
            dp[i][0] += 1
            stones[i] //= 2
        while stones[i] % 5 == 0:
            dp[i][1] += 1
            stones[i] //= 5
    
    answer = min(dp[N-1][0], dp[N-1][1])
    print(answer)
    