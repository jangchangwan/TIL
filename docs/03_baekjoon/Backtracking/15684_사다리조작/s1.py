# 15684_사다리조작_문제풀이
# 2022-04-12

import sys

input = sys.stdin.readline


def dfs(count, num):
    global min_ans
    if count >= min_ans:
        return
    if check():
        min_ans = count
        return
    for idx in range(num+1, len(candidates)):
        i, j = candidates[idx]
        if lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lines[i][j] = 1
            dfs(count+1, idx)
            lines[i][j] = 0


def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if lines[j][now] == 1:
                now += 1
            elif lines[j][now-1] == 1:
                now -= 1

        if i != now:
            return False
    return True


n, m, h = map(int, input().split())
lines = [[0] * (n+1) for _ in range(h+1)]
candidates = []
min_ans = 4
# 데이터 받아오기
for _ in range(m):
    x, y = map(int, input().split())
    lines[x][y] = 1

for i in range(1, h+1):
    for j in range(1, n):
        if lines[i][j-1] == 0 and lines[i][j] == 0 and lines[i][j+1] == 0:
            candidates.append([i, j])

dfs(0, -1)

print(min_ans if min_ans < 4 else -1)