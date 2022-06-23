# 14500_테트로미노_문제풀이
# 2022-04-01
# 한 지점에서 4번 이동했을때 갈수 있는 경우의수를 모두 표현 한 것이라고 생각함
# DFS 4번 이동했을때 최대값을 찾았을때 값과 동일하지 않을까 생각
# ㅗ 모양은 DFS 로 이동했을 경우 모양이 구현 X 추가 조건필요
# DFS 한번 이동했을경우 ni ,nj 가 아닌 i, j 로 DFS 동작하면 될것

# 시간 초과
# 가지치기를 해야함 => max값을 가지치기 하기위해서 한번 시행했을때 최대값을 알아야함


import sys
sys.stdin = open('input.txt', 'r')


def DFS(r, c, cnt, res):
    global ans
    # 종료 조건 : 4번 동작했을경우
    if cnt == 4:
        ans = max(ans, res)
        return

    # 시행햇수 * 최대값을 했을경우 ans 보다 작거나 같을 경우 검토 X
    if res + max_value * (4 - cnt) <= ans:
        return

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = r + dr
        nc = c + dc

        if (0 <= nr < N) and (0 <= nc < M) and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            if cnt == 2:
                DFS(r, c, cnt + 1, res + arr[nr][nc])
            DFS(nr, nc, cnt + 1, res + arr[nr][nc])
            visited[nr][nc] = 0


# 세로 가로
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

max_value = 0
for i in range(N):
    temp_max = max(arr[i])
    if temp_max > max_value:
        max_value = temp_max


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            visited[i][j] = 1
            DFS(i, j, 1, arr[i][j])
            visited[i][j] = 0

print(ans)
