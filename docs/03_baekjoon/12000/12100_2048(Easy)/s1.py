# 12100_2048_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')
from copy import deepcopy
# 숫자이동
def move(board, dir):
    if dir == 0:
        for i in range(N):
            top = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = temp

    elif dir == 1:  # 서쪽
        for i in range(N):
            top = 0
            for j in range(1, N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] = temp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = temp

    elif dir == 2:  # 남쪽
        for j in range(N):
            top = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = temp

    else:
        for j in range(N):
            top = 0
            for i in range(1, N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = temp
    return board


# 횟수확인
def DFS(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    else:
        for i in range(4):
            temp = move(deepcopy(board), i)
            DFS(temp, cnt+1)


# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
DFS(arr, 0)
print(ans)