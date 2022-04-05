# 5688_세제곱근을찾아라_문제풀이
# 2022-03-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = -1
    # 역순으로 진행
    for i in range(int(N**(1/3))+1, 0, -1):
        x = i * i * i
        # 찾을경우 숫자를 적는다
        if x == N:
            ans = i
            break
        if x < N:
            break
    print('#{} {}'.format(tc, ans))