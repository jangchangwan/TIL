# 2115_벌꿀채취_문제풀이
# 2022-04-02
import sys
sys.stdin = open('input.txt', 'r')


def DFS(r, c, cnt, total, res):
    global ans, result

    # 종료조건
    if total > C:
        return
    #
    if cnt == M:
        if total > ans:
            ans = total
            result = res
        elif total == ans:
            result = max(result, res)

        return

    DFS(r, c+1, cnt+1, total+arr[r][c+1], res+double_arr[r][c+1])


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    double_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            double_arr[i][j] = arr[i][j] ** 2
    ans = 0
    result = 0
    for i in range(N):
        for j in range(N - M + 1):
            DFS(i, j, 0, arr[i][j], double_arr[i][j])

    print('#{} {}'.format(tc, result))