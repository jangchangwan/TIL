import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
N = 9
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 초기값 1
    result = 1
    # 가로줄 검사
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
        # 합이 45가 아닐경우 0으로 리턴
        if row_sum != 45:
            result = 0
            break
    # 새로줄 검사
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += arr[i][j]
            # 합이 45가 아닐경우 0으로 리턴
        if col_sum != 45:
            result = 0
            break

    # 3x3 검사
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            kh_sum = 0
            for k in range(0, 3):
                for h in range(0, 3):
                    kh_sum += arr[i+k][j+h]
            if kh_sum != 45:
                result = 0
                break

    ans = result
    print('#{} {}'.format(t, ans))
