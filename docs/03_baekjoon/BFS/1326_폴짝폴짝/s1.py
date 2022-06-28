# 1326_폴짝폴짝
# 2022-06-28
# 1차원 BFS

from collections import deque


def bfs(start, end, N):
    q = deque()
    q.append(start-1)
    visited = [-1]*N
    visited[start-1] = 0
    while q:
        node = q.popleft()
        for n in range(N):
            # 배수이고 방문하지않은 곳일 경우
            if (n-node) % bridge[node] == 0 and visited[n] == -1:
                q.append(n)
                visited[n] = visited[node] + 1
                # 도착점에 도달했을 경우
                if n == end-1:
                    return visited[n]
    return -1


N = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())

ans = bfs(start, end, N)

print(ans)