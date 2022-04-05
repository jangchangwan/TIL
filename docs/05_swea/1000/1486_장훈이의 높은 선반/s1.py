# 1486_장훈이의 높은선반_문제풀이
# 2022-03-18

import sys
sys.stdin = open('input_2.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    arr = list(map(int, input().split()))
    min_res = 999999999
    # 부분 집합 구하기
    for i in range(1 << N):
        res = 0
        for j in range(N):
            if i & (1 << j):
                res += arr[j]

        if B <= res < min_res:
            min_res = res
    ans = min_res - B
    print('#{} {}'.format(tc, ans))