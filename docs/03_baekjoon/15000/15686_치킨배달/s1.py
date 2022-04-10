# 15686_치킨배달_문제풀이
# 2022-04-11

'''
집과 치킨집의 좌표를 뽑아낸다음
살릴 치킨집은 조합 알고리즘으록 구해서
BFS로 각집에서의 최단거리를 구한다.
시간초과
'''
import sys
sys.stdin = open('input.txt', 'r')


# 조합 만들기
def chicken_order(n, picked, toPick):
    global orders
    if toPick == 0:
        orders.append(picked[:])
        return

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            chicken_order(n, picked, toPick - 1)
            picked.pop()


# 최단 경로
def BFS(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    visited[sr][sc] = 1
    while front != rear:
        front += 1
        r, c = queue[front]
        if arr[r][c] == 2:
            return visited[r][c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                rear += 1
    # 못찾은 경우
    return -1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# N : 행렬의 크기
# M : 치킨집 수
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))
            arr[i][j] = 0


# 순서뽑기
orders = []
chicken_order(len(chicken), [], M)

min_cnt = 987654321
# 조합만큼 반복
for order in orders:
    cnt = 0
    for i in order:
        r, c = chicken[i]
        arr[r][c] = 2

    for h in house:
        visited = [[0] * N for _ in range(N)]
        temp = BFS(h[0], h[1])
        cnt += (temp-1)

    for i in order:
        r, c = chicken[i]
        arr[r][c] = 0

    min_cnt = min(min_cnt, cnt)

print(cnt)