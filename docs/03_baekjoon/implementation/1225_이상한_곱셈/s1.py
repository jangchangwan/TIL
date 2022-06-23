# 1225_이상한_곱셈_문제풀이
# 2022-04-16

import sys
sys.stdin = open('input.txt', 'r')

A, B = map(str, input().split())

total = 0
for a in A:
    for b in B:
        total += (int(a) * int(b))

print(total)