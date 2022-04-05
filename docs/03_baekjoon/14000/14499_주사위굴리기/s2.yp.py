# 14499_주사위-굴리기_문제풀이
# 2022-03-28
import sys
sys.stdin = open('input.txt', 'r')


def chk(order, c, r):
    x = c + dx[order]
    y = r + dy[order]
    if 0 <= x < N and 0 <= y < M:
        # 동
        if order == 0:
            dice[1][1], dice[1][2], dice[3][1], dice[1][0] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
            print(dice[1][1])
        # 서
        elif order == 1:
            dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
            print(dice[1][1])
        # 북
        elif order == 2:
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
            print(dice[1][1])
        # 남
        elif order == 3:
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
            print(dice[1][1])
        # 0 만나면 아래면 값 넣어줌.
        if arr[x][y] == 0:
            arr[x][y] = dice[3][1]
        # 0 아니면 바닥면에 자리 값 넣어줌.
        else:
            dice[3][1] = arr[x][y]
            arr[x][y] = 0

        return x, y
    # 범위 밖이면 리턴
    else:
        return c, r


N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
# 초기 주사위 모양
dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for i in range(K):
    x, y = chk(command[i]-1, x, y)