# 1992_쿼드트리
# 2022-07-07
# 재귀

def dfs(r, c, n):
    temp = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if temp != arr[i][j]:
                print('(', end='')
                dfs(r, c, n // 2)
                dfs(r, c + n // 2, n // 2)
                dfs(r + n // 2, c, n // 2)
                dfs(r + n // 2, c + n // 2, n // 2)
                print(')', end='')
                return

    if temp == '0':
        print(0, end='')
        return
    elif temp == '1':
        print(1, end='')
        return


N = int(input())
arr = [list(input()) for _ in range(N)]

dfs(0, 0, N)