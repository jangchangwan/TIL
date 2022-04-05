import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    mid = (N // 2) + 1

    top_sum = 0
    for i in range(mid-1):
        top_sum += arr[i][mid-1]
        for k in range(1, i+1):
            top_sum += arr[i][mid - 1 + k]
            top_sum += arr[i][mid - 1 - k]

    bottom_sum = 0
    for i in range(N-1, mid-1, -1):
        bottom_sum += arr[i][mid - 1]
        for k in range(1, N-i):
            bottom_sum += arr[i][mid - 1 + k]
            bottom_sum += arr[i][mid - 1 - k]
    center_sum = 0
    for i in range(N):
        center_sum += arr[mid-1][i]

    total_sum = top_sum + bottom_sum + center_sum
    print('#{} {}'.format(tc, total_sum))