import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대값
    max_sum = 0
    # 방향
    dir_a = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_b = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(N):
        for j in range(N):
            now_sum_a = arr[i][j]
            now_sum_b = arr[i][j]
            for p in range(1, P+1):
                for k in range(4):
                    # 상하좌우
                    ni_a = i + dir_a[k][0] * p
                    nj_a = j + dir_a[k][1] * p
                    # 대각선
                    ni_b = i + dir_b[k][0] * p
                    nj_b = j + dir_b[k][1] * p
                    if (0 <= ni_a < N) and (0 <= nj_a < N):
                        now_sum_a += arr[ni_a][nj_a]
                    if (0 <= ni_b < N) and (0 <= nj_b < N):
                        now_sum_b += arr[ni_b][nj_b]

            if now_sum_a > max_sum:
                max_sum = now_sum_a
            if now_sum_b > max_sum:
                max_sum = now_sum_b

    ans = max_sum
    print('#{} {}'.format(t, ans))