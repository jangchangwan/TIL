# 1238_Contact_문제풀이
# 2022-03-16

import sys
sys.stdin = open('input.txt', 'r')

T = 10


for tc in range(1, T+1):
    N, start = map(int, input().split())
    N_lst = list(map(int, input().split()))
    # 연결 리스트 만들기
    arr = [[] for _ in range(101)]
    for i in range(0, N, 2):
        # 중복 없애주기
        if N_lst[i+1] in arr[N_lst[i]]:
            continue
        arr[N_lst[i]].append(N_lst[i+1])

    # 최대 100명이므로
    visited = [0] * 101
    queue = [start]
    visited[start] = 1
    front = -1
    rear = 0
    while front != rear:
        front += 1
        temp = queue[front]
        for t in arr[temp]:
            if visited[t] == 0:
                queue.append(t)
                visited[t] = visited[temp] + 1
                rear += 1

    max_num = max(visited)
    ans = 0
    for i in range(1, 101):
        if visited[i] == max_num and i > ans:
            ans = i
    print('#{} {}'.format(tc, ans))
