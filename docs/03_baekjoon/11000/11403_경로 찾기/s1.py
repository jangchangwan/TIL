# 11403_경로 찾기_문제풀이
# 2022-05-30

import sys
sys.stdin = open('input.txt', 'r')


def DFS(node):
    for i in range(N):
        if visited[i] == 0 and arr[node][i] == 1:
            visited[i] = 1
            DFS(i)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    visited = [0 for i in range(N)]
    DFS(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()