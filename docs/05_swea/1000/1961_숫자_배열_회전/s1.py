# 1961_숫자_배열_회전_문제풀이
# 2022-02-18
import sys
sys.stdin = open('input.txt', 'r')


def rotate_arr(arr, num):
    new_arr = [[0]*num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for n in range(N)]

    arr_90 = rotate_arr(arr, N)
    arr_180 = rotate_arr(arr_90, N)
    arr_270 = rotate_arr(arr_180, N)

    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for k in range(N):
            print(arr_180[i][k], end='')
        print(end=' ')
        for h in range(N):
            print(arr_270[i][h], end='')
        print()

