import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    base_arr = [list(map(int, input().split())) for _ in range(N)]

    dir_a = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_b = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

    max_result = 0
    for i in range(N):
        for j in range(N):
            total_A_num = base_arr[i][j]
            total_B_num = base_arr[i][j]
            for m in range(1, M):
                for k in range(4):
                    ni_a = i + dir_a[k][0] * m
                    nj_a = j + dir_a[k][1] * m
                    if (0 <= ni_a < N) and (0 <= nj_a < N):
                        total_A_num += base_arr[ni_a][nj_a]
                    ni_b = i + dir_b[k][0] * m
                    nj_b = j + dir_b[k][1] * m
                    if (0 <= ni_b < N) and (0 <= nj_b < N):
                        total_B_num += base_arr[ni_b][nj_b]
            if total_A_num > max_result:
                max_result = total_A_num
            if total_B_num > max_result:
                max_result = total_B_num
    print('#{} {}'.format(tc, max_result))