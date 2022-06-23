# 5073_삼각형과 세 변_문제풀이
# 2022-04-30

import sys
sys.stdin = open('input.txt', 'r')

while True:
    # 입력
    Line = list(map(int, input().split()))

    # 종료조건
    if Line[0] == 0 and Line[1] == 0 and Line[2] == 0:
        break

    # 삼각형 조건 만족
    Line.sort()
    if Line[0] + Line[1] <= Line[2]:
        print('Invalid')

    else:
        if Line[0] == Line[1] and Line[1] == Line[2]:
            print('Equilateral')
        elif Line[0] == Line[1] or Line[1] == Line[2] or Line[0] == Line[2]:
            print('Isosceles')
        else:
            print('Scalene')