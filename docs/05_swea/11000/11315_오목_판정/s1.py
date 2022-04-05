# 11315_오목_판정_문제풀이
# 2022-02-27
# 6이상될경우 4_3 의 경우도 오목으로 체크해서 안된다.
# 단순이 카운터만 세주기때문에 이렇게 쓰면안될듯

import sys
sys.stdin = open('input.txt', 'r')


# 5개 이상연속되는 부분 찾기
def concave(arr_1):
    cnt = 0
    for n in arr_1:
        if n >= 5:
            cnt += 1
    return cnt

 
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    base_arr = [list(map(str, input())) for _ in range(N)]
    # 세로
    row_N = [0] * N
    # 가로
    col_N = [0] * N
    # 우하향 대각선
    diag_A_N = [0] * (2 * N)
    # 좌하향 대각선
    diag_B_N = [0] * (2 * N)

    for i in range(N):
        for j in range(N):
            if base_arr[i][j] == 'o':
                row_N[i] += 1
                col_N[j] += 1
                diag_A_N[N+j-i-1] += 1
                diag_B_N[i+j] += 1

    res = concave(row_N) + concave(col_N) + concave(diag_A_N) + concave(diag_B_N)

    if res == 0:
        print('#{} NO'.format(tc))
    else:
        print('#{} YES'.format(tc))
