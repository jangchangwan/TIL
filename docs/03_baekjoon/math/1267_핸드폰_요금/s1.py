# 1267_핸드폰_요금_문제풀이
# 2022-04-17

import sys
sys.stdin = open('input.txt', 'r')

'''
영식이는 30초마다 10원
민식이는 60초 15

'''


N = int(input())
N_lst = list(map(int, input().split()))
Y, M = 0, 0
for n in N_lst:
    Y += (n // 30 + 1) * 10
    M += (n // 60 + 1) * 15

if Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)
else:
    print('Y', 'M', M)
