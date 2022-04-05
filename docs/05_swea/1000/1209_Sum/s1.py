import sys

sys.stdin = open('input.txt', 'r')

T = 10

for t in range(T):
    # input 값 받아오기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 결과 변수
    max_sum = 0
    # 가로합
    for i in range(100):
        sum_nums = 0
        for j in range(100):
            sum_nums += arr[i][j]
        if sum_nums > max_sum:
            max_sum = sum_nums
    # 세로합
    for j in range(100):
        sum_nums = 0
        for i in range(100):
            sum_nums += arr[i][j]
        if sum_nums > max_sum:
            max_sum = sum_nums
    # 대각선 type 1
    sum_nums = 0
    for i in range(100):
        sum_nums += arr[i][i]
    if sum_nums > max_sum:
        max_sum = sum_nums

    # 대각선 type 2
    sum_nums = 0
    for i in range(100):
        sum_nums += arr[i][99-i]
    if sum_nums > max_sum:
        max_sum = sum_nums
    ans = max_sum
    print('#{} {}'.format(N, ans))