# 1800_인터넷 설치
# 2022-06-26
# 다익스트라 + 이분탐색
# Pypy3 / 296ms

# N번째 컴퓨터에 인터넷 연결했을때 최소비용

import heapq

def BFS(start, end):
    queue = []
    dis = [inf] * (N+1)
    heapq.heappush(queue, [0, start])
    dis[start] = 0

    while queue:
        cost, idx = heapq.heappop(queue)

        for a in graph[idx]:
            if a[1] > end:
                if cost + 1 < dis[a[0]]:
                    dis[a[0]] = cost + 1
                    heapq.heappush(queue, [cost + 1, a[0]])
            else:
                if cost < dis[a[0]]:
                    dis[a[0]] = cost
                    heapq.heappush(queue, [cost, a[0]])

    if dis[N] > K:
        return False
    else:
        return True


inf = 987654321

N, P, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(P):
    start, end, cost = map(int, input().split())
    # 양방향
    graph[start].append([end, cost])
    graph[end].append([start, cost])

# 드는 비용으로 이분탐색
left, right=0, 1000001
answer = inf

while left <= right:
    mid = (left+right)//2
    # mid 이하의 cost로 인터넷 설치가 가능한 경우
    if BFS(1, mid):
        right = mid-1
        answer = mid
    # 안되는 경우
    else:
        left = mid+1

if answer == inf:
    print(-1)
else:
    print(answer)