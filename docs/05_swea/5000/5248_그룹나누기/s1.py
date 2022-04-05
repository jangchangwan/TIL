# 5248_그룹나누기_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')


def BFS(i):
    global visited
    front = -1
    rear = 0
    queue = [i]
    visited[i] = 1
    while front != rear:
        front += 1
        temp = queue[front]
        for t in arr[temp]:
            if visited[t] == 0:
                queue.append(t)
                visited[t] = 1
                rear += 1
    return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    M_lst = list(map(int, input().split()))

    visited = [0] * (N + 1)
    arr = [[] for _ in range(N+1)]

    for i in range(0, len(M_lst), 2):
        arr[M_lst[i]].append(M_lst[i+1])
        arr[M_lst[i+1]].append(M_lst[i])
        
    ans = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            BFS(i)
            ans += 1
    
    print('#{} {}'.format(tc, ans))