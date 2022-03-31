# 5209_최소_생산_비용_문제풀이
# 2022-03-31
import sys
sys.stdin = open('input.txt', 'r')


def DFS(i, cnt, total):
    global min_ans
    if cnt == N:
        min_ans = min(min_ans, total)
        return
    if total >= min_ans:
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            DFS(i+1, cnt + 1, total + arr[i][j])
            visited[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문체크
    visited = [0] * N
    min_ans = 0
    for i in range(N):
        min_ans += arr[i][i]

    DFS(0, 0, 0)
    print('#{} {}'.format(tc, min_ans))