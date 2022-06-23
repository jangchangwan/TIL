# 11729_하노이 탑 이동순서_문제풀이
# 2022-04-28

import sys
sys.stdin = open('input.txt', 'r')


def DFS(n, one, two, three):
    if n == N:
        print(one, three)

    else:
        DFS(n + 1, one, three, two)
        print(one, three)
        DFS(n + 1, two, one, three)


N = int(input())

ans = 1
for i in range(N-1):
    ans = ans * 2 + 1

print(ans)
DFS(1, 1, 2, 3)