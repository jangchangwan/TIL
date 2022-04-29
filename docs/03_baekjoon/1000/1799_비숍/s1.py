# 1799_비숍_문제풀이
# 2022-04-29

import sys
sys.stdin = open('input.txt', 'r')


'''
비숍을 놓을 수있는곳에서 시작을하고
놓을 경우 대각선을 다채운뒤
1로 가득찼을경우 동작횟수를 비교하여 최대값을 출력한다.
'''

def DFS(ans, r, c, cnt):
    global max_ans
    # 종료조건
    if cnt == N*N:
        max_ans = max(max_ans, ans)
    else:
        temp = []
        temp += BFS_1(r, c)
        temp += BFS_2(r, c)
        temp += BFS_3(r, c)
        temp += BFS_4(r, c)
        temp = list(set(temp))
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    DFS(ans+1, i, j, cnt+len(temp))

        for er, ec in temp:
            arr[er][ec] = 1


# 비숍이 갈수있는 곳을 채우는 곳
def BFS_1(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    arr[sr][sc] = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        nr = r + 1
        nc = c + 1
        if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc]:
            arr[nr][nc] = 0
            queue.append((nr, nc))
            rear += 1
    return queue


def BFS_2(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    arr[sr][sc] = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        nr = r + 1
        nc = c - 1
        if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc]:
            arr[nr][nc] = 0
            queue.append((nr, nc))
            rear += 1
    return queue


def BFS_3(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    arr[sr][sc] = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        nr = r - 1
        nc = c + 1
        if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc]:
            arr[nr][nc] = 0
            queue.append((nr, nc))
            rear += 1
    return queue


def BFS_4(sr, sc):
    front = -1
    rear = 0
    queue = [(sr, sc)]
    arr[sr][sc] = 0
    while front != rear:
        front += 1
        r, c = queue[front]
        nr = r - 1
        nc = c - 1
        if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc]:
            arr[nr][nc] = 0
            queue.append((nr, nc))
            rear += 1
    return queue


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 갯수확인
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt += 1


max_ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            DFS(1, i, j, cnt+1)

print(max_ans)