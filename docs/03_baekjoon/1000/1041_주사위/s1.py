# 1041_주사위_문제풀이
# 2022-05-01

import sys
sys.stdin = open('input.txt', 'r')

'''
면이 1개 보이는 블록 개수 : 4 * (N - 2) * (N - 1) + (N - 2) ** 2   
면이 2개 보이는 블록 개수 : 4 * (N - 1) + 4 * (N - 2)
면이 3개 보이는 블록 개수 : 4 (가장 상단 모서리 4개)
'''

N = int(input())
dice = list(map(int, input().split()))

ans = 0
min_lists = []
if N == 1:
    dice.sort()
    for i in range(5):
        ans += dice[i]
else:
    min_lists.append(min(dice[0], dice[5]))
    min_lists.append(min(dice[1], dice[4]))
    min_lists.append(min(dice[2], dice[3]))
    min_lists.sort()

    # 1, 2, 3 면의 주사위 최소값
    min1 = min_lists[0]
    min2 = min_lists[0] + min_lists[1]
    min3 = sum(min_lists)

    # 1, 2, 3 면의 주사위 개수
    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    ans += min1 * n1
    ans += min2 * n2
    ans += min3 * n3
print(ans)
