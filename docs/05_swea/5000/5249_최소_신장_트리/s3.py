# 5249_최소_신장_트리_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')


def MST_prim(s):
    key = [INF] * (N+1)
    visited = [0] * (N+1)
    key[s] = 0
    for _ in range(N+1):
        minindex = -1
        min_val = INF
        for i in range(N+1):
            if visited[i] == 0 and key[i] < min_val:
                min_val = key[i]
                minindex = i

        visited[minindex] = 1
        for v, val in Graph[minindex]:
            if visited[v] == 0 and val < key[v]:
                key[v] = val
    return key


INF = 1000000000
T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())

    Graph = [[] for _ in range(N+1)]

    for _ in range(E):
        start, end, w = map(int, input().split())
        Graph[start].append((end, w))
        Graph[end].append((start, w))

    key = MST_prim(0)

    print('#{} {}'.format(tc, sum(key)))
