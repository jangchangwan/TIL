# 1915_가장 큰 정사각형_문제풀이
# 2022-05-12

from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

'''
N, M 에서 작은 수를 찾기
arr         visited
0 1 0 0     1 1 1 1
0 1 1 1     1 1 1 1
1 1 1 0     1 1 2 1
0 0 1 0     1 1 1 1

max 값 2 => 4
'''


def check(r, c):
    if arr[r-1][c-1] == arr[r][c-1]:
        if arr[r][c-1] == arr[r-1][c]:
            return True
    return False


# 입력
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[1] * M for _ in range(N)]


max_cnt = 0
# 1 x N 또는 M x 1 일때 max_cnt 초기값 찾기
for i in range(N):
    if arr[i][0]:
        max_cnt = 1
for j in range(M):
    if arr[0][j]:
        max_cnt = 1

for i in range(1, N):
    for j in range(1, M):
        if arr[i][j] and check(i, j):
            visited[i][j] = min(visited[i-1][j-1], visited[i-1][j], visited[i][j-1]) + 1
            if max_cnt < visited[i][j]:
                max_cnt = visited[i][j]
# 출력
print(max_cnt**2)

