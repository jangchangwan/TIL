def DFS(n, lst, cnt, ssum):
    global sol
    if cnt > C:
        return
    if n == M:
        sol = max(sol, ssum)
        return

    DFS(n + 1, lst, cnt + lst[n], ssum + lst[n] ** 2)
    DFS(n + 1, lst, cnt, ssum)


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # mem
    mem = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            sol = 0
            DFS(0, arr[i][j:j + M], 0, 0)
            mem[i][j] = sol

    for i1 in range(N):
        for j1 in range(N - M + 1):
            for i2 in range(i1, N):
                sj = 0
                if i1 == i2:
                    sj = j1 + M
                for j2 in range(sj, N - M + 1):
                    ans = max(ans, mem[i1][j1] + mem[i2][j2])

    print(f'#{test_case} {ans}')