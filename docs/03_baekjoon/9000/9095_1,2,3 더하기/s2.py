# 9095_1,2,3, 더하기_문제풀이
# 2022-05-12

import sys
sys.stdin = open('input.txt', 'r')

'''
    1   2   3   4   5   6   7   8   9   10

T   1   2   4   7   13  24  44  81  149 274

f(n) = f(n-3) + f(n-2) + f(n-1)
'''


T = int(input())

for t in range(T):

    N = int(input())
    DP = [0, 1, 2, 4]
    for i in range(4, N+1):
        DP.append(DP[i-3] + DP[i-2] + DP[i-1])
    print(DP[N])