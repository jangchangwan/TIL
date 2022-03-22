# 2105_디저트카페_문제풀이
# 2022-03-22

import sys
sys.stdin = open('input.txt', 'r')


def DFS(r, c, d, cnt):
    global ans

    # 마름모로 이동하기
    if d < 3:
        end = d + 2
    else:
        end = d + 1

    for k in range(d, end):
        nr = r + dir[k][0]
        nc = c + dir[k][1]
        # 도착했을 경우
        if start_r == nr and start_c == nc:
            if cnt > ans:
                ans = cnt
            return

        # 조건 성립 시
        if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0 and dessert_arr[N_arr[nr][nc]] == 0:
            # 방문체크
            dessert_arr[N_arr[nr][nc]] = 1
            visited[nr][nc] = 1
            DFS(nr, nc, k, cnt + 1)
            # 복구
            visited[nr][nc] = 0
            dessert_arr[N_arr[nr][nc]] = 0
    return -1


# 방향 ( 좌하 , 우하 , 우상 , 좌상 )
dir = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 체크 리스트
    visited = [[0] * N for _ in range(N)]
    dessert_arr = [0] * 101
    ans = -1
    for i in range(N):
        for j in range(N):

            start_r = i
            start_c = j
            dessert_arr[N_arr[i][j]] = 1
            visited[i][j] = 1
            DFS(i, j, 0, 1)
            visited[i][j] = 0
            dessert_arr[N_arr[i][j]] = 0

    print('#{} {}'.format(tc, ans))