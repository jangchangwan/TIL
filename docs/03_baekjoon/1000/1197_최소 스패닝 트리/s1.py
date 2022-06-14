# 1197_최소 스패닝 트리
# 2022-06-12

import heapq


V, E = map(int, input().split())
visited = [0] * (V+1)
arr = [[] for _ in range(V+1)]
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    arr[s].append([w, e])
    arr[e].append([w, s])


answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if visited[s] == 0:
        visited[s] = 1
        answer += w
        cnt += 1
        for i in arr[s]:
            heapq.heappush(heap, i)

print(answer)