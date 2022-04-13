# 1753_최단경로_문제풀이
# 2022-04-07

# 가중치와 최단경로를 보고 다익스트라 문제인것으로 파악했고
# prim알고리즘을 사용해서 풀면 답이 나올거같았다
import sys
sys.stdin = open('input.txt', 'r')


def MST_prim(s):
    key = [INF] * (V+1)
    visited = [0] * (V+1)
    key[s] = 0
    for _ in range(V+1):
        min_index = -1
        min_value = INF
        for i in range(V+1):
            if visited[i] == 0 and key[i] < min_value:
                min_value = key[i]
                min_index = i

        visited[min_index] = 1
        for v, val in Graph[min_index]:
            if visited[v] == 0 and val < key[v]:
                key[v] = val
    return key[1:]


INF = 1000000
V, E = map(int, input().split())
# 출발점
K = int(input())

Graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, w = map(int, input().split())
    Graph[start].append((end, w))
    # Graph[end].append((start, w))

key = MST_prim(K)
for i in key:
    if i == INF:
        print('INF')
    else:
        print(i)