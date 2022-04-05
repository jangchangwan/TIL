# 5249_최소_신장_트리_문제풀이
# 2022-04-05

import sys
sys.stdin = open('input.txt', 'r')


def DFS(node, dis, cnt):
    global ans

    if dis >= ans:
        return
    if cnt == V:

        ans = min(ans, dis)
        return
    else:
        if arr[node]:

            for i in arr[node]:
                if i[0] in visited:
                    continue
                visited.append(i[0])
                DFS(i[0], dis + i[1], cnt + 1)
                visited.pop()
    return


T = int(input())

for tc in range(1, T+1):
    V , E = map(int, input().split())

    arr = [[] for _ in range(V+1)]

    for t in range(E):
        start, end, w = map(int, input().split())
        arr[start].append((end, w))
        arr[end].append((start, w))

    ans = 10000000 * 10
    visited = []

    DFS(0, 0, 0)
    print('#{} {}'.format(tc, ans))