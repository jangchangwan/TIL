# 14442_벽 부수고 이동하기 2_문제풀이
# 2022-04-30


import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

'''
front, rear 를 사용했을경우 메모리 초과가 떳다

deque를 사용해야할듯 -> 메모리 해결 , 시간초과 발생
sys.stdin.readline으로 데이터를 받아와봄 = > 시간초과
BFS문 안에 if 조건문 순서를 변경하여 조건을 줄인다.

'''


def BFS():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        r, c, cnt = queue.popleft()
        # 종료조건
        if r == (N-1) and c == (M-1):
            return visited[r][c][cnt]
        # 4 방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 밖을 벗어나지 않고 지나간곳이 아닌 경우
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc][cnt]:
                # 벽을 안 부슬 경우
                if not arr[nr][nc]:
                    visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                    queue.append([nr, nc, cnt])
                # 벽을 부슬 수 있는 경우
                elif cnt < K:
                    visited[nr][nc][cnt + 1] = visited[r][c][cnt] + 1
                    queue.append([nr, nc, cnt + 1])
    # 못찾은 경우
    return -1


# 방향
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 입력
N, M, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
print(BFS())