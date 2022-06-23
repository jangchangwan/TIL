# 2644_촌수계산_문제풀이
# 2022-03-21
import sys
sys.stdin = open('input.txt', 'r')


def bfs(arr, start):
    global visited
    queue = [start]
    while queue:
        temp = queue.pop(0)
        for t in arr[temp]:
            if visited[t] == 0:
                visited[t] = visited[temp] + 1
                queue.append(t)
    return -1


N = int(input())
start, end = map(int, input().split())

link_cnt = int(input())
link_list = [list() for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(link_cnt):
    x, y = map(int, input().split())
    link_list[x].append(y)
    link_list[y].append(x)

bfs(link_list, start)
if visited[end] > 0:
    print(visited[end])
else:
    print(-1)
