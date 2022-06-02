# 11725_트리의 부모 찾기_문제풀이
# 2022-05-28

import sys
sys.stdin = open('input.txt', 'r')


def BFS():
    q = [1]
    front = -1
    rear = 0
    while front != rear:
        front += 1
        node = q[front]
        for i in tree[node]:
            if visited[i] == 0:
                visited[i] = node
                q.append(i)
                rear += 1


# 입력
N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

BFS()

for i in visited[2:]:
    print(i)