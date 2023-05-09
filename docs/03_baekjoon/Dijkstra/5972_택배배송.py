import heapq
import sys
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
dijkstra(1)
print(dis[N])