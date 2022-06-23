# 9251_LCS_문제풀이
# 2022-04-14

import sys
sys.stdin = open('input.txt', 'r')


word_1 = input()
word_2 = input()


dp = [[0] * (len(word_2) + 1) for _ in range(len(word_1) + 1)]

for i in range(1, len(word_1) + 1):
    for j in range(1, len(word_2) + 1):
        if word_1[i - 1] == word_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])