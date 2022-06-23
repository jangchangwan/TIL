# 2527_직사각형_문제풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')

T = 4

for t in range(T):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 범위가 큰값을 뒤로 보낸다
    if x1 > x2:
        x1, x2 = x2, x1
        p1, p2 = p2, p1
    if y1 > y2:
        y1, y2 = y2, y1
        q1, q2 = q2, q1
    # 비교

    if x2 > p1 or y2 > q1:
        ans = 'd'
    elif x2 == p1 and y2 == q1:
        ans = 'c'
    elif (x2 == p1 and y2 < q1) or (y2 == q1 and x2 < p1):
        ans = 'b'
    else:
        ans = 'a'

    print(ans)