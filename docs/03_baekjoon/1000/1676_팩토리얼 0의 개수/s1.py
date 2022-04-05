# 1676_팩토리얼 0의 개수_문제풀이
# 2022-03-30

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

cnt = 0
cnt_2 = 0
cnt_5 = 0
for i in range(1, N+1):

    while i > 1:
        if i % 10 == 0:
            i //= 10
            cnt += 1
        elif i % 2 == 0:
            i //= 2
            cnt_2 += 1
        elif i % 5 == 0:
            i //= 5
            cnt_5 += 1
        else:
            break

while cnt_2 and cnt_5:
    cnt_2 -= 1
    cnt_5 -= 1
    cnt += 1

print(cnt)