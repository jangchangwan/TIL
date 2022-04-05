# 14502_연구소 풀이
# 2022-03-15

from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

candidates = deque()
virus = []
answer = n * m
wall = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            candidates.append(i * m + j)
        elif lst[i][j] == 2:
            virus.append([i, j])
        else:
            wall += 1

queue = deque()
queue.append([])

while 1:
    if len(queue[0]) == 3:
        break
    tmp = queue.popleft()
    if tmp:
        M = max(tmp)
    for i in candidates:
        if tmp:
            if i <= M:
                continue

        queue.append(tmp + [i])

for i in queue:
    for j in range(3):
        i[j] = [i[j] // m, i[j] % m]

## 여기까지가 조합 만들기
# queue에는 벽의 후보가 들어있.

for idx in range(5, len(queue) + 5):
    res = 0
    candidate = queue[idx - 5]

    for i, j in candidate:
        lst[i][j] = idx
    use = deque(virus)

    while use:

        x, y = use.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and (lst[nx][ny] != 1 and lst[nx][ny] != idx and lst[nx][ny] != 2):
                lst[nx][ny] = idx
                res += 1
                if answer <= res:
                    break
                use.append([nx, ny])
    if answer > res:
        answer = res

print(n * m - wall - answer - 3 - len(virus))