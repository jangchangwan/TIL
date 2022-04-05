# 2667_단지번호붙이기_문제풀이
# 2022-03-21
import sys
sys.stdin = open('input.txt', 'r')


def dfs(arr, i, j, cnt):
    global visited
    check = 1
    stack = [(i, j)]
    # 처음들어간곳도 방문체크를한다.
    visited[i][j] = cnt
    while stack:
        row, col = stack.pop()
        for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = row + dir[0]
            nj = col + dir[1]
            # 범위 벗어나지 X  and 아파트가 좌표에 존재하고 and 방문하지 않는 곳일 경우
            if (0 <= ni < N) and (0 <= nj < N) and (arr[ni][nj] == 1) and (visited[ni][nj] == 0):
                # 조건에 맞는 좌표를 스택에 추가한다
                stack.append((ni, nj))
                # 방문 체크한다
                visited[ni][nj] = cnt
                check += 1
    return check


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 1
cnt_list= []
for i in range(N):
    for j in range(N):
        # 방문하지 않고 아파트인곳에 들어간다
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt_list.append(dfs(arr, i, j, cnt))
            cnt += 1

print(cnt-1)
cnt_list.sort()
for c in cnt_list:
    print(c)

