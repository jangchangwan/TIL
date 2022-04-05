import sys
sys.stdin = open('input.txt', 'r')


def DFS(n, r, c, num):
    if n == 7:
        result.add(num)
        return
    for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if (0 <= nr < 4) and (0 <= nc < 4):
            DFS(n+1, nr, nc, num + arr[nr][nc])
    return


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    # 중복 제거
    result = set()
    for i in range(4):
        for j in range(4):
            DFS(1, i, j, arr[i][j])

    ans = len(result)
    print('#{} {}'.format(tc, ans))