import sys
sys.stdin = open('input.txt','r')

def is_next(i, j, ni, nj):
    if number[ni][nj] == number[i][j]-7:
        return True
    elif number[ni][nj] == number[i][j]-6:
        return True
    elif number[ni][nj] == number[i][j]-5:
        return True
    elif number[ni][nj] == number[i][j]-1:
        return True
    elif number[ni][nj] == number[i][j]+1:
        return True
    elif number[ni][nj] == number[i][j]+6:
        return True
    else:
        return False


def dfs(i, j, cnt, temp):
    global max_value

    # 종료조건
    if cnt == 3:
        if max_value < temp:
            max_value = temp
        return

    # 도는조건
    for di, dj in pos:
        ni = i + di
        nj = j + dj
        if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] != 1:
            visited[ni][nj] = 1
            if cnt == 1:
                dfs(i, j, cnt + 1, temp + base[ni][nj])
            dfs(ni, nj, cnt+1, temp+base[ni][nj])
            visited[ni][nj] = 0


T = int(input())
for tc in range(1, 1+T):
    W, H = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(H)]
    number = list()
    for i in range(H):
        temp = list()
        for j in range(1, W+1):
            temp.append(i*W+j)
        number.append(temp)

    visited = [[0]*W for _ in range(H)]
    max_value = -1
    pos = [[0, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

    for i in range(H):
        for j in range(W):
            visited[i][j] = 1
            dfs(i, j, 0, base[i][j])
            visited[i][j] = 0

    print(f'#{tc} {max_value**2}')