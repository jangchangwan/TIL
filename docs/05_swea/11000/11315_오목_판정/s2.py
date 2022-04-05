import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    base_arr = [list(map(str, input())) for _ in range(N)]

    dir = [(0, 1), (1, 0), (1, 1), (1, -1)]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if base_arr[i][j] == 'o':
                    cnt = 1
                else:
                    cnt = 0
                ni = i + dir[k][0]
                nj = j + dir[k][1]
                while (0 <= ni < N) and (0 <= nj < N):
                    if base_arr[ni][nj] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt >= 5:
                        ans = 'YES'
                    ni += dir[k][0]
                    nj += dir[k][1]

    print('#{} {}'.format(tc, ans))
