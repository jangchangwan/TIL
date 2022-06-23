# 1240_노드사이의 거리_문제풀이
# 2022-06-24
# Python 3 / 460 ms
# BFS ( 넓이 우선 탐색 )

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    queue = deque()
    queue.append(start)
    visited = [-1] * (N + 1)
    visited[start] = 0
    while queue:
        temp = queue.popleft()
        if temp == end:
            break
        for node, dis in graph[temp]:
            if visited[node] == -1:
                visited[node] = visited[temp] + dis
                queue.append((node))
    return visited[end]


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end, dis = map(int, input().split())
    graph[start].append((end, dis))
    graph[end].append((start, dis))

for _ in range(M):
    start, end = map(int, input().split())
    answer = BFS(start, end)
    print(answer)