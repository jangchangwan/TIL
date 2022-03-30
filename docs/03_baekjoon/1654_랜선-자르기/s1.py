# 1654_랜선-자르기_문제풀이
# 2022-03-30
# 시간 초과
import sys
sys.stdin = open('input.txt', 'r')

K, N = map(int, input().split())

K_lst = [int(input()) for _ in range(K)]

total = sum(K_lst)
for t in range(total, 0, -N):
    temp = t // N
    cnt = 0
    for k in K_lst:
        cnt += k // temp

    if cnt == N:
        break
print(temp)
