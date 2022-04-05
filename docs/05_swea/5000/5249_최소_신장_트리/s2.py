# 5249_최소_신장_트리 (Prim 알고리즘)
# 2022-04-05

import sys

sys.stdin = open('input.txt', 'r')


def prim(start):
    key = [int(1e9)] * (V + 1)
    mst = [0] * (V + 1)
    key[start] = 0
    for _ in range(V + 1):
        min_idx = -1
        min_val = int(1e9)
        for i in range(V + 1):
            if not mst[i] and key[i] < min_val:
                min_val = key[i]
                min_idx = i

        mst[min_idx] = 1

        for v, val in g[min_idx]:
            if not mst[v] and val < key[v]:
                key[v] = val

    return key


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    info = list(list(map(int, input().split())) for _ in range(E))
    g = [[] for _ in range(V + 1)]

    for e in info:
        g[e[0]].append((e[1], e[2]))
        g[e[1]].append((e[0], e[2]))

    key = prim(0)

    print("#{} {}".format(tc, sum(key)))