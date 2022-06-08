# 9466_팀 프로젝트_문제풀이
# 2022-06-08

import sys
sys.setrecursionlimit(10 ** 6)

def DFS(node):
    global ans
    visited[node] = True
    cycle.append(node)
    temp = students[node]

    # 이미방문했을 경우
    if visited[temp]:
        # 싸이클 안에 있는 경우 팀 완성
        if temp in cycle:
            ans += cycle[cycle.index(temp):]
        return
    # 아닐경우 계속탐색
    else:
        DFS(temp)


T = int(input())

for tc in range(T):
    # 입력
    N = int(input())
    # 인덱스 맞추기 위해 [0] 추가
    students = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    ans = []
    # 탐색
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            DFS(i)
    # 출력
    print(N - len(ans))