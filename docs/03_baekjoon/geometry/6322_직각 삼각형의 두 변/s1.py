# 6322_직각 삼각형의 두 변_문제풀이
# 2022-04-30

import sys
sys.stdin = open('input.txt', 'r')

t = 1
while True:
    # 입력
    tri = list(map(int, input().split()))

    # 종료조건
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    print(f'Triangle #{t}')

    if tri[2] == -1:
        print("c = %.3f" % ((tri[0] ** 2 + tri[1] ** 2) ** 0.5))
    elif max(tri[0], tri[1]) >= tri[2]:
        print("Impossible.")
    elif tri[0] == -1:
        print("a = %.3f" % ((tri[2] ** 2 - tri[1] ** 2) ** 0.5))
    elif tri[1] == -1:
        print("b = %.3f" % ((tri[2] ** 2 - tri[0] ** 2) ** 0.5))

    print()
    t += 1