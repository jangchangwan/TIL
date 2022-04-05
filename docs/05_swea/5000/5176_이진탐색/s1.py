# 5176_이진탐색_문제풀이
#2022-03-17

import sys
sys.stdin = open('input.txt', 'r')


# 중위순회
def in_order(T):
    global cnt
    if T <= N:
        in_order(T*2)
        ans[T] = cnt
        cnt += 1
        in_order(T*2 + 1)


T = int(input())

for tc in range(1, T+1):
    cnt = 1
    N = int(input())
    tree = [0] * (N + 1)
    for n in range(1, N+1):
        tree[n] = n
    ans = [0] * (N + 1)
    in_order(1)
    print('#{} {} {}'.format(tc, ans[1], ans[N//2]))