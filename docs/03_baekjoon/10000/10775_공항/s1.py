# 10775_공항_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
P = list(int(input()) for _ in range(P))
ans = 0
for p in P:
    res = find(p)
    if res == 0:
        break
    parent[res] = parent[res - 1]
    ans += 1
print(ans)