# 9095_1,2,3, 더하기_문제풀이
# 2022-05-12

import sys
sys.stdin = open('input.txt', 'r')


def DFS(total):
    global cnt

    # 종료조건
    if total == N:
        cnt += 1
        return
    # 가지치기
    elif total > N:
        return

    else:
        for i in range(1,N):
            DFS(total + i)


T = int(input())

for t in range(T):
    cnt = 0

    N = int(input())
    ans = N
    DFS(0)
    print(cnt)