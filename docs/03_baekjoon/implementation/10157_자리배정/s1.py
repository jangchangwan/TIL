# 10157_자리배정_문제풀이
# 2022-02-25

import sys
sys.stdin = open('input.txt', 'r')

row, col = map(int, input().split())

K = int(input())


arr = [[0]*col for _ in range(row)]
ans = [0, 0]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ri = rj = k = 0
if K > (row * col):
    print(0)

else:
    for i in range(1, row*col+1):
        arr[ri][rj] = i
        if i == K:
            print(ri+1, rj+1)
            break
        ri += di[k]
        rj += dj[k]
        if (ri < 0) or (ri >= row) or (rj < 0) or (rj >= col) or arr[ri][rj] != 0:
            ri -= di[k]
            rj -= dj[k]

            k = (k + 1) % 4

            ri += di[k]
            rj += dj[k]
