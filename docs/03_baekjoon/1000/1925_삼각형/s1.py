# 1925_삼각형
# 2022-06-17
import math

point = [list(map(int, input().split())) for _ in range(3)]

Line_1 = math.pow(point[0][0] - point[1][0], 2) + math.pow(point[0][1] - point[1][1], 2)
Line_2 = math.pow(point[1][0] - point[2][0], 2) + math.pow(point[1][1] - point[2][1], 2)
Line_3 = math.pow(point[2][0] - point[0][0], 2) + math.pow(point[2][1] - point[0][1], 2)

Line_1, Line_2, Line_3 = sorted([Line_1, Line_2, Line_3])

if (point[0][1] - point[1][1]) * (point[0][0] - point[2][0]) == (point[0][1] - point[2][1]) * (point[0][0] - point[1][0]):
    print('X')

# 정삼각형
elif Line_1 == Line_2 and Line_2 == Line_3:
    print('JungTriangle')
# 두 변의 길이가 같을 때
elif Line_1 == Line_2 or Line_2 == Line_3 or Line_3 == Line_1:
    if Line_3 == Line_1 + Line_2:
        print('Jikkak2Triangle')
    elif Line_3 < Line_1 + Line_2:
        print('Yeahkak2Triangle')
    else:
        print('Dunkak2Triangle')
# 세 변의 길이가 다를 때
else:
    if Line_3 == Line_1 + Line_2:
        print('JikkakTriangle')
    elif Line_3 < Line_1 + Line_2:
        print('YeahkakTriangle')
    else:
        print('DunkakTriangle')