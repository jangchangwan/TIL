# 1167_트리의지름_문제풀이
# 2022-04-24

import sys
sys.stdin = open('input.txt', 'r')


def BFS(s):
    visited = [-1] * (N + 1)
    queue = [s]
    front = -1
    rear = 0
    visited[s] = 0
    res = [0, 0]
    while front != rear:
        front += 1
        x = queue[front]
        for end, dis in arr[x]:
            if visited[end] == -1:
                visited[end] = visited[x] + dis
                queue.append(end)
                rear += 1
                if res[1] < visited[end]:
                    res = end, visited[end]
    return res


N = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(N):
    N_lst = list(map(int, input().split()))
    n = N_lst[0]
    idx = 1
    while True:
        if N_lst[idx] == -1:
            break
        arr[n].append((N_lst[idx], N_lst[idx+1]))

        idx += 2

node, dis = BFS(1)
node, dis = BFS(node)
print(dis)
