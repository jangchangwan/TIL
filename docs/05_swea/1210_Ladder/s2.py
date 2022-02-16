import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * 102 for _ in range(102)]
    for i in range(1, 101):
        arr[i] = [0] + list(map(int, input().split())) + [0]
    for j in range(1, 101):
        if arr[100][j] == 2:
            break
    nj = j
    ni = 99

    while 1:
        if ni == 1:
            break
        if arr[ni][nj-1] == 1:
            while arr[ni][nj-1] != 0:
                nj -= 1
        elif arr[ni][nj+1] == 1:
            while arr[ni][nj+1] != 0:
                nj += 1
        ni -= 1
    print('{} {}'.format(N, nj-1))