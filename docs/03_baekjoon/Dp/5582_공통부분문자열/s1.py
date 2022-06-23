# 5582_공통_부분_문자열_문제풀이
# 2022-04-27
# Pypy3 / 240816 KB / 468 ms

import sys
sys.stdin = open('input.txt', 'r')

str_a = input()
str_b = input()

answer = 0
dp = [[0 for _ in range(len(str_b) + 1)] for _ in range(len(str_a) + 1)]
for i in range(len(str_a)):
    for j in range(len(str_b)):
        if str_a[i] == str_b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
            answer = max(answer, dp[i + 1][j + 1])

print(answer)
