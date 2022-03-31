# 5251_최소-이동-거리_문제풀이
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')


def DFS(node, dis):
    global ans
    # 초과 할경우 탐색 X
    if dis >= ans:
        return
    # 성립할 경우 최소값
    if node == N:
        ans = min(ans, dis)
        return
    else:
        if move[node]:
            for i in move[node]:
                if i[0] in visited:
                    continue
                visited.append(i[0])
                DFS(i[0], dis + i[1])
                visited.pop()


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    move = [[] for _ in range(N)]

    for _ in range(E):
        start, end, w = map(int, input().split())
        move[start].append((end, w))

    ans = 10000000
    visited = []
    DFS(0, 0)
    print('#{} {}'.format(tc, ans))