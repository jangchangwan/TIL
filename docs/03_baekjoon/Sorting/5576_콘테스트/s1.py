# 5576_콘테스트_문제풀이
# 2022-05-16

import sys
sys.stdin = open('input.txt', 'r')

W_team = [int(input()) for _ in range(10)]
K_team = [int(input()) for _ in range(10)]

W_team.sort()
K_team.sort()

W_ans, K_ans = 0, 0
for i in range(7, 10):
    W_ans += W_team[i]
    K_ans += K_team[i]

print(W_ans, K_ans)
