# 14889_스타트와_링크_문제풀이
# 2022-04-01
# 실패

import sys
sys.stdin = open('input.txt', 'r')


def dfs(idx, cnt):
    global ans, checked
    if visited in checked:
        return
    # 종료 조건
    if cnt == N // 2:
        # 반대의 경우 동작 x
        for k in range(len(visited)):
            if visited[k]:
                visited_reverse[k] = 0
            else:
                visited_reverse[k] = 1
        checked.append(visited_reverse)

        A, B = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    A += arr[i][j] + arr[j][i]
                elif visited[i] == 0 and visited[j] == 0:
                    B += arr[i][j] + arr[j][i]
        ans = min(ans, abs(A - B))
        return

    # 팀 선정
    for i in range(idx, N):

        if visited[i]:
            continue
        visited[i] = 1
        dfs(i + 1, cnt + 1)
        visited[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
checked = []
visited = [0 for _ in range(N)]
visited_reverse = [0 for _ in range(N)]
ans = 9999999
dfs(0, 0)
print(ans)