# 4615_재미있는_오셀로_게임_문제풀이
# 2022-03-24

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    # 판 생성
    doll_arr = [[0]*N for _ in range(N)]
    mid = N // 2
    doll_arr[mid][mid] = 2
    doll_arr[mid-1][mid] = 1
    doll_arr[mid][mid-1] = 1
    doll_arr[mid-1][mid-1] = 2
    # 8방향
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # 반복
    for n in range(K):
        col, row, user = map(int, input().split())
        # 인덱스 맞추기
        row -= 1
        col -= 1

        temp = list()
        # 8방향
        for i in range(8):
            dr, dc = delta[i]
            nr, nc = row+dr, col+dc
            while True:
                if (0 > nr) or (nr >= N) or (0 > nc) or (nc >= N):
                    temp = list()
                    break
                # 다른 색돌뒤에 같은색돌이 아닌 빈공간을 만날경우
                if doll_arr[nr][nc] == 0:
                    temp = list()
                    break
                # 같은돌을 만날경우 나온다
                elif doll_arr[nr][nc] == user:
                    break
                # 다른돌을 만날경우 그 좌표를 담는다.
                else:
                    temp.append((nr, nc))
                # 계속 그쪽으로 간다
                nr += dr
                nc += dc
            # temp 리스트 안에 있는것 반복
            for rr, rc in temp:
                if user == 1:
                    doll_arr[rr][rc] = 1
                else:
                    doll_arr[rr][rc] = 2
        doll_arr[row][col] = user

    white = black = 0
    for i in range(N):
        for j in range(N):
            if doll_arr[i][j] == 1:
                black += 1
            elif doll_arr[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(t, black, white))