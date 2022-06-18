# 2252_줄세우기
# 2022-06-15

from collections import deque

N, M = map(int, input().split())


graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
queue = deque()
answer = []
for i in range(M):
    winner, loser = map(int, input().split())
    graph[winner].append(loser)
    inDegree[loser] += 1

for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    temp = queue.popleft()
    answer.append(temp)
    for i in graph[temp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*answer)