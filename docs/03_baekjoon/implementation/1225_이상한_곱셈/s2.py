# 1225_이상한_곱셈_문제풀이
# 2022-04-16

import sys
sys.stdin = open('input.txt', 'r')

A, B = map(str, input().split())


sum_a = 0
sum_b = 0
for a in A:
    sum_a += int(a)

for b in B:
    sum_b += int(b)

print(sum_a*sum_b)