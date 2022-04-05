# 5014_스타트링크_문제풀이
# 2022_03_17
import sys
sys.stdin = open('input.txt', 'r')


def BFS(s, e, u, d):
    global visited
    queue = [s]
    front = -1
    rear = 0
    visited[s] = 1
    while front != rear:
        front += 1
        now = queue[front]
        if e == now:
            return print(visited[e]-1)
        for di in [u, -d]:
            after = now + di
            if (0 < after <= floor) and visited[after] == 0:
                queue.append(after)
                visited[after] = visited[now] + 1
                rear += 1

    return print("use the stairs")


floor, start, end, up, down = map(int, input().split())
# 방문
visited = [0] * (floor + 1)
BFS(start, end, up, down)


