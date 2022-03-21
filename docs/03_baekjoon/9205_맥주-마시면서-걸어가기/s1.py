import sys
sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    global visited
    queue = [(i, j)]
    front = -1
    rear = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        # 현재 위치에서 도착위치로 갈 수 있으면
        if abs(end_x - r) + abs(end_y - c) <= 1000:
            return 'happy'
        # 현재 위치에서 갈 수 있는 편의점 탐색
        for i in range(N):
            if visited[i] == 0:
                nr, nc = dir_lst[i]
                if abs(nr - r) + abs(nc - c) <= 1000:
                    queue.append((nr, nc))
                    visited[i] = 1
                    rear += 1
    # 도착점 까지 못갔을 경우
    return 'sad'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start_x, start_y = map(int, input().split())
    result = 'happy'
    visited = [0 for i in range(N+1)]
    dir_lst = []
    for i in range(N):
        x, y = map(int, input().split())
        dir_lst.append((x, y))
    end_x, end_y = map(int, input().split())
    ans = BFS(start_x, start_y)
    print(ans)