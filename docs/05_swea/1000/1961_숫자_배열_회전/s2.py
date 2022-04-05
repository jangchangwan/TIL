# 1961_숫자_배열_회전_문제풀이
# 2022-02-18
import sys
sys.stdin = open('input.txt', 'r')


def rotate_arr(arr):
    new_arr = list(zip(*arr[::-1]))
    return new_arr


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for n in range(N)]

    arr_90 = rotate_arr(arr)
    arr_180 = rotate_arr(arr_90)
    arr_270 = rotate_arr(arr_180)

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
