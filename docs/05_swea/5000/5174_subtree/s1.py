# 5174_subtree_문제풀이
# 2022-03-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, start = map(int, input().split())
    N_lst = list(map(int, input().split()))
    edge_lst = [[] for _ in range(N+2)]
    # 연결리스트 생성
    for i in range(N):
        edge_lst[N_lst[i*2]].append(N_lst[i*2+1])
    print(edge_lst)
    queue = [start]
    front = -1
    rear = 0
    # 자식노드 queue에 담아주기
    while front != rear:
        front += 1
        temp = queue[front]
        for edge in edge_lst[temp]:
            queue.append(edge)
            rear += 1

    ans = len(queue)
    print('#{} {}'.format(tc, ans))