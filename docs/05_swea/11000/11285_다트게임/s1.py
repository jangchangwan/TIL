import sys
import math
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    point = 0
    for n in range(N):
        x, y = map(int, input().split())
        dis_xy = math.sqrt(x**2+y**2)
        p = (dis_xy // 20) + 1
        if p > 11:
            p = 11

        point += (11 - p)

    print('#{} {}'.format(tc, int(point)))