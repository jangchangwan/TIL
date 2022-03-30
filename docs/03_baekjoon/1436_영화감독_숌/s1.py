# baekjoon_1436_영화감독_숌
# 2022-03-25

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

num = 665
cnt = 0

while cnt != N:
    temp_cnt = 0
    for n in str(num):
        if n == '6':
            temp_cnt += 1
        elif n != '6':
            temp_cnt = 0
        if temp_cnt >= 3:
            cnt += 1
            break
    num += 1

ans = num
print(ans-1)