# 1697_숨바꼭질_문제풀이
# 2022-03-21

import sys
sys.stdin = open('input.txt', 'r')


def bfs():
    q = [start]

    while q:
        x = q.pop(0)
        if x == end:
            return dist[x]
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= max_time and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return


max_time = 100000
dist = [0] * (1000000 + 1)

start, end = map(int, input().split())

ans = bfs()
print(ans)