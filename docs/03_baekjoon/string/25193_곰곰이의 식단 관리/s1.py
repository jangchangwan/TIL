# 25193_곰곰이의 식단 관리
# 2022-06-30
# 문자열

import math

N = int(input())
word = list(input())

chicken = 0

for w in word:
    if w == 'C':
        chicken += 1

other = N - chicken + 1

print(math.ceil(chicken / other))