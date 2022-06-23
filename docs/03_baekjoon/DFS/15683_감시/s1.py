# 15683_감시_문제풀이
# 2022-04-10

import sys
sys.stdin = open('input.txt', 'r')

'''
완전탐색해서 CCTV가 있는 좌표와 값이 0인 갯수를 찾은 뒤
사각지대를 찾을 때마다 사각지대를 하나씩 제거하고
모두 탐색했을 때 최소값과 비교하는 DFS를 구현
'''

def DFS(n, ans):
    global min_ans
    # 종료조건 : 모든 cctv 탐색
    if n == len(cctv_list):
        min_ans = min(ans, min_ans)
        return

    r, c = cctv_list[n]
    cctv_num = arr[r][c]
    for dir in cctv_type[cctv_num]:
        total_cnt = 0
        # 복구하기 위해서
        temp = []
        for d in dir:
            nr = r + dr[d]
            nc = c + dc[d]
            cnt = 0
            while (0 <= nr < N) and (0 <= nc < M) and arr[nr][nc] != 6:
                if arr[nr][nc] == 0:
                    cnt += 1
                    arr[nr][nc] = 7
                    temp.append((nr, nc))
                nr += dr[d]
                nc += dc[d]
            total_cnt += cnt
        DFS(n + 1, ans - total_cnt)
        for nr, nc in temp:
            arr[nr][nc] = 0


# 4방향 : 북, 남, 동, 서
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 1 ~ 5번 까지 경우의 수
cctv_type = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

# row, col
N, M = map(int, input().split())
# Map
arr = [list(map(int, input().split())) for _ in range(N)]

cctv_list = []
answer = 0
for i in range(N):
    for j in range(M):
        # cctv 좌표 찾기
        if 0 < arr[i][j] < 6:
            cctv_list.append((i, j))
        # 사각지대
        elif arr[i][j] == 0:
            answer += 1

min_ans = 10000000000
DFS(0, answer)
print(min_ans)
