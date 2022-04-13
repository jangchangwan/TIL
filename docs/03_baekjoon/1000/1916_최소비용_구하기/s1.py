# 1916_최소비용_구하기
# 2022-04-13
import sys
sys.stdin = open('input.txt', 'r')
import heapq

def my_heapq(start, end):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if visited[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return visited[end]


INF = 987654321

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [INF for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())
answer = my_heapq(start, end)
print(answer)