# 5532_방학 숙제
# 2022-05-06

import sys
sys.stdin = open('input.txt', 'r')

d = [int(input()) for _ in range(5)]

a = []
for i in range(1, 3):
    a.append(d[i] // d[i+2] + 1 if d[i] % d[i+2] else d[i] // d[i+2])

res = a[0] if a[0] > a[1] else a[1]
print(d[0] - res)