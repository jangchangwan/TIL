# 2117_홈_방범_서비스_문제풀이
# 2022-03-23

import sys
sys.stdin = open('input.txt', 'r')


def BFS(r, c):
    global max_cnt
    visited = [[0] * map_size for _ in range(map_size)]
    visited[r][c] = 1
    queue = [(r, c)]
    client = map_arr[r][c]
    front = 0
    rear = 0
    dis = 1
    while dis < (map_size + 2):
        queue_length = len(queue[front:(rear+1)])
        for _ in range(queue_length):
            r, c = queue[front]
            front += 1
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if (0 <= nr < map_size) and (0 <= nc < map_size) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    rear += 1
                    # 고객이 있을 경우 체크
                    if map_arr[nr][nc] == 1:
                        client += 1
        # 이익이 0 이상일 경우 최대값 비교
        if client * cost - cost_lst[dis+1] >= 0:
            max_cnt = max(client, max_cnt)
        dis += 1


T = int(input())
# K 범위에 따른 비용
cost_lst = [0]*23
for i in range(1, 23):
    cost = i * i + (i - 1) * (i - 1)
    cost_lst[i] = cost
# 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    map_size, cost = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(map_size)]

    max_cnt = 1
    for i in range(map_size):
        for j in range(map_size):
            BFS(i, j)
    print('#{} {}'.format(tc, max_cnt))