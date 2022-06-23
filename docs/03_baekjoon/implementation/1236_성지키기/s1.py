# 1236_성지키기_문제풀이
# 2022-04-16

import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())

arr = [list(map(str, input())) for _ in range(n)]
a, b = 0, 0

for i in range(n):
    if "X" not in arr[i]:
        a += 1

for j in range(m):
    if "X" not in [arr[i][j] for i in range(n)]:
        b += 1

print(max(a, b))