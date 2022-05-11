# 2293_동전 1_문제풀이
# 2022-05-11
# 백트래킹 / 8% 시간초과 실패

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def DFS(total, order):
    global cnt, visited

    # 종료조건
    if total == K:
        if order in visited:
            return
        else:
            visited.append(order[:])
            cnt += 1
            return
    # 가지치기
    elif total > K:
        return
    else:
        for i in range(N):
            order[i] += 1
            DFS(total+N_lst[i], order)
            order[i] -= 1


N, K = map(int, input().split())
N_lst = [int(input()) for _ in range(N)]
order = [0]*N
N_lst.sort(reverse=True)
visited = [[]]
cnt = 0
DFS(0, order)
print(cnt)