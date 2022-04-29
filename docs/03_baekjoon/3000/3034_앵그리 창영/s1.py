# 3034_앵그리 창영_문제풀이
# 2022-04-29
import math

N, W, H = map(int, input().split())
res = math.sqrt(math.pow(W, 2) + math.pow(H, 2))

for _ in range(N):
    heat = int(input())
    print('NE') if heat > res else print('DA')