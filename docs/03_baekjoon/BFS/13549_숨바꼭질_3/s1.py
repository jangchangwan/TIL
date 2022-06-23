# 13549_숨바꼭질_3_문제풀이
# 2022-04-14

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def bfs(start):
    front = -1
    rear = 0
    queue = [(start, 0)]
    visited = [0] * 100001
    visited[start] = 1

    while queue:
        front += 1
        loc, time = queue[front]
        if loc == K:  # 동생을 찾으면 리턴
            return time

        # 순간 이동 - 우선순위 0
        if loc < 50001 and visited[loc * 2] == 0:
            queue.append([loc * 2, time])
            visited[loc * 2] = 1
            rear += 1
        # x-1 이동 - 우선순위 1
        if loc > 0 and visited[loc - 1] == 0:
            queue.append([loc - 1, time + 1])
            visited[loc - 1] = 1
            rear += 1
        # x+1 이동 - 우선순위 2
        if loc < 100000 and visited[loc + 1] == 0:
            queue.append([loc + 1, time + 1])
            visited[loc + 1] = 1
            rear += 1


N, K = map(int, input().split())
print(bfs(N))