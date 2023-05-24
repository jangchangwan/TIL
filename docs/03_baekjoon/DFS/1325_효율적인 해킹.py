"""
N : 컴퓨터 갯수

한번에 가장 많이 해킹할수있는 번호
"""

def BFS(start):
    cnt = 1
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    queue = [start]
    front = -1
    rear = 0
    
    while front != rear:
        front += 1
        now = queue[front]
        
        for v in graph[now]:
            if visited[v] == 0:
                rear += 1
                visited[v] = 1
                queue.append(v)
                cnt += 1
    
    return cnt
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[end].append(start)
    
result = []
max_count = 0
for i in range(1, N+1):
    count = BFS(i)
    max_count = max(max_count, count)
    result.append((i, count))


answer = []
for idx, cnt in result:
    if cnt == max_count:
        answer.append(idx)
        
print(*answer)