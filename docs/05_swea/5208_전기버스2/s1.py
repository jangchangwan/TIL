# 5208_전기버스2_문제풀이
# 2022-03-31

import sys
sys.stdin = open('input.txt', 'r')


def DFS(node, cnt):
    global min_ans
    # 횟수가 초과할경우 중단
    if cnt >= min_ans:
        return
    # 도착지까지 도착한 경우
    if node >= N-1:
        min_ans = min(min_ans, cnt)
        return
    # 3, 2
    for i in range(node+N_arr[node], node, -1):
        DFS(i, cnt + 1)


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    N_arr = arr[1:]+[0]*(N-1)

    min_ans = 999999999
    DFS(0, 0)
    print('#{} {}'.format(tc, min_ans-1))