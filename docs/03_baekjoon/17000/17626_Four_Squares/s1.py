# 17626_Four_Squares_문제풀이
# 2022-04-09

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

DP = [0, 1] + [0] * (N - 1)

for i in range(2, N + 1):
    minValue = 10000000000
    j = 1
    while j ** 2 <= i:
        minValue = min(minValue, DP[i-(j**2)])
        j += 1
    DP[i] = i + minValue

print(DP[N])
print(DP)