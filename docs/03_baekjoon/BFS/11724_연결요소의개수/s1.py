# 11724_연결요소의개수_문제풀이
# 2022-04-22

import sys
sys.stdin = open('input.txt', 'r')


def BFS(s):
    global visited
    front = -1
    rear = 0
    queue = [s]
    visited[s] = 1
    while front != rear:
        front += 1
        temp = queue[front]
        for v in N_lst[temp]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = 1
                rear += 1
    return


# 정점과 간선 수
N, M = map(int, input().split())

N_lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    N_lst[start].append(end)
    N_lst[end].append(start)

cnt = 0
for n in range(1, N+1):
    if visited[n] == 0:
        BFS(n)
        cnt += 1

print(cnt)