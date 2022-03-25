# 5648_원자-소멸-시뮬레이션-문제풀이
# 2022-03-25

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    i = 0
    visited = []
    while i != len(atom):
        j = 1
        while j != len(atom):
            # 상 -> 하
            if (atom[i][2] == 0) and (atom[j][2] == 1) and (atom[i][0] == atom[j][0]):
                if atom[i][1] < atom[j][1]:
                    ans += (atom[i][3] + atom[j][3])
                    atom.pop(j)
                    continue
            # 상 -> 하
            elif (atom[i][2] == 1) and (atom[j][2] == 0) and (atom[i][0] == atom[j][0]):
                if atom[i][1] > atom[j][1]:
                    ans += (atom[i][3] + atom[j][3])
                    atom.pop(j)
                    continue
            # 좌 -> 우
            elif (atom[i][2] == 2) and (atom[j][2] == 3) and (atom[i][1] == atom[j][1]):
                if atom[i][0] > atom[j][0]:
                    ans += (atom[i][3] + atom[j][3])
                    atom.pop(j)
                    continue
            # 우 -> 좌
            elif (atom[i][2] == 3) and (atom[j][2] == 2) and (atom[i][1] == atom[j][1]):
                if atom[i][0] < atom[j][0]:
                    ans += (atom[i][3] + atom[j][3])
                    atom.pop(j)
                    continue
            j += 1
        i += 1
    print('#{} {}'.format(tc, ans))