# 1861_정사각형_방_문제풀이
# 2022-03-16

import sys
sys.stdin = open('input.txt', 'r')


# 제일 멀리 갔을 떄 구하기
def BFS(i, j):
    front = -1
    rear = 0
    queue =[(i, j)]
    # 방문 초기화
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    while front != rear:
        front += 1
        r, c = queue[front]
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = r + di
            nj = c + dj
            if (0 <= ni < N) and (0 <= nj < N) and visited[ni][nj] == 0 and (N_arr[ni][nj] == N_arr[r][c] + 1):
                queue.append((ni, nj))
                visited[ni][nj] = visited[r][c] + 1
                rear += 1
    return visited[r][c]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = [list(map(int, input().split())) for _ in range(N)]

    min_num = 10000000
    max_dis = 0
    ans_lst= []
    # 모든 좌표 반복
    for i in range(N):
        for j in range(N):
            ans = BFS(i, j)
            # 최대 거리
            if ans >= max_dis:
                max_dis = ans
                ans_lst.append((N_arr[i][j], max_dis))
    for i in ans_lst:
        if i[1] == max_dis and i[0] < min_num:
            min_num = i[0]

    print('#{} {} {}'.format(tc, min_num, max_dis))