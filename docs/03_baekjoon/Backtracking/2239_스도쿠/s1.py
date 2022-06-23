# 2239_스도쿠_문제풀이
# 2022-06-07

import sys
sys.stdin = open('input.txt', 'r')


def check(r, c, num):
    # 행
    for j in range(9):
        if arr[r][j] == num:
            return False
    # 열
    for i in range(9):
        if arr[i][c] == num:
            return False
    # 3 x 3
    rr = (r // 3) * 3
    rc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[rr+i][rc+j] == num:
                return False
    return True


def DFS(idx):
    global arr, flag
    # 종료조건
    if idx == len(zeros):
        flag = True
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end='')
            print()
        return
    if flag:
        return
    else:
        nr, nc = zeros[idx]
        for num in range(1, 10):
            if check(nr, nc, num):
                arr[nr][nc] = num
                DFS(idx + 1)
                arr[nr][nc] = 0


arr = [list(input()) for _ in range(9)]
flag = False
zeros = []
for i in range(9):
    for j in range(9):
        arr[i][j] = int(arr[i][j])
        if arr[i][j] == 0:
            zeros.append((i, j))

DFS(0)
