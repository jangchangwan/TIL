# 9465_스티커_문제풀이
# 2022-04-14

import sys
sys.stdin = open('input.txt', 'r')

'''
    2줄로 이루어진 데이터이고 하나를 선택할경우 상하좌우를 선택못하므로
    경우의수는 2가지밖에없다.
    이럴경우 앞에값이 너무작은경우 건너뛰고 했을때가 더 높은 정수를 얻을수도 있다.
    한칸더 확인해보자
    정답은 나왔지만 만약에 예외가 존재할거같다
'''


T = int(input())


for t in range(T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(2)]

    for j in range(1, N):
        if j == 1:
            arr[0][j] += arr[1][j - 1]
            arr[1][j] += arr[0][j - 1]
        else:
            arr[0][j] += max(arr[1][j - 1], arr[1][j - 2])
            arr[1][j] += max(arr[0][j - 1], arr[0][j - 2])

    print(max(arr[0][-1], arr[1][-1]))