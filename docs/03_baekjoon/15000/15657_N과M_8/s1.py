# 15654_N과M_8_문제풀이
# 2022-04-13


'''
    백트래킹으로 순열구하는 문제
    방문 리스트를 만들어서 없을경우만 동작하여
    M 만큼 반복한후 출력하게 만든다
'''

import sys
sys.stdin = open('input.txt', 'r')


def DFS(cnt, idx, visited):
    if cnt == M:
        print(*visited)
        return
    for num in range(idx, N):
        visited.append(N_lst[num])
        DFS(cnt + 1, num, visited)
        visited.pop()


N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
N_lst.sort()
DFS(0, 0, [])