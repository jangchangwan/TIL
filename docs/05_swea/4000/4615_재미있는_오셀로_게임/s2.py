import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[N]*(N+2) for _ in range(N+2)]
    arr[N//2][N//2] = 1
    arr[N//2+1][N//2+1] = 1
    arr[N//2][N//2 +1] = 0
    arr[N//2 +1][N//2] = 0

    print(arr)

    # 북, 북동, 동, 남동, 남, 남서, 서, 북서
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for m in range(M):
        x, y, color = map(int, input().split())
        # 컬러 0, 1로 표시하고 싶어서 1 빼기. 흑 : 0, 백 : 1.
        color = color - 1

        # if N not input.txt arr:
        #     break

        for i in range(8):
            for a in range(N-1, 1, -1):
                if 1 <= x + a*dx[i] <= N and 1 <= y + a*dy[i] <= N:
                    if arr[y+dy[i]][x+dx[i]] == 1 - color and arr[y + a*dy[i]][x + a*dx[i]] == color:
                        # 중간에 빈 칸이 있나 없나 확인해야함
                        tmp = 0
                        for b in range(1, a):
                            if arr[y + b * dy[i]][x + b * dx[i]] == N:
                                tmp = 0
                            else:
                                tmp = 1

                        # N이 없으면 그 사이에 있는 거 다 바꿔줌
                        if tmp == 1:
                            for b in range(1, a):
                                arr[y + b * dy[i]][x + b * dx[i]] = color
                            arr[y][x] = color
    black = white = 0

    for j in range(1, N+1):
        for k in range(1, N+1):
            if arr[j][k] == 0:
                black += 1
            elif arr[j][k] == 1:
                white += 1


    print('#{} {} {}'.format(tc, black, white))