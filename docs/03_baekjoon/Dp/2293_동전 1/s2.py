# 2293_동전 1_문제풀이
# 2022-05-11
# DP
# 116332 KB / 136 ms

'''
경우의 수
    1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1
2   0   1   1   2   2   3   3   4   4   5
5   0   0   0   0   1   1   2   2   3   4

T   1   2   2   3   4   5   6   7   8   10


f(k) = f(k) + f(k - coin)
'''
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
N_lst = [int(input()) for _ in range(N)]

order = [0]*(K+1)
order[0] = 1
for n in N_lst:
    for i in range(n, K+1):
        order[i] += order[i-n]

print(order[K])