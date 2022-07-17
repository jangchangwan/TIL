# 2210_숫자판
# 2022-07-17
# DFS

def DFS(cnt, r, c, number):
    global visited
    if cnt == 6:
        if number not in visited:
            visited.append(number[:])
        return
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < 5) and (0 <= nc < 5):
                DFS(cnt+1, nr, nc, number+str(arr[nr][nc]))


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

arr = [list(map(int, input().split())) for _ in range(5)]

visited = []

for i in range(5):
    for j in range(5):
        DFS(1, i, j, str(arr[i][j]))

answer = len(visited)
print(answer)