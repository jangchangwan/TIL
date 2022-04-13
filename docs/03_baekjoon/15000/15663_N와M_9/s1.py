# 15654_N과M_9_문제풀이
# 2022-04-13


'''
    백트래킹으로 순열구하는 문제
    방문 리스트를 만들어서 없을경우만 동작하여
    M 만큼 반복한후 출력하게 만든다
'''

import sys
sys.stdin = open('input.txt', 'r')


def DFS(depth, N, M):
    if depth == M:
        tmp = ' '.join(map(str, out))
        if tmp not in all_out:
            all_out.append(tmp)
        return
    for i in range(N):
        if not visited[i]:
            out.append(N_lst[i])
            visited[i] = True
            DFS(depth+1, N, M)
            out.pop()
            visited[i] = False


N, M = map(int, input().split())
N_lst = list(map(int, sys.stdin.readline().split()))
N_lst.sort()
visited = [False] * N
out = []
all_out = []

DFS(0, N, M)
for i in all_out:
    print(i)