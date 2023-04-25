"""
문제
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

예제 입력 1 
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
"""
import sys

input = sys.stdin.readline
# 최단거리 탐색
def BFS(sr, sc):
    global result
    
    queue = [(sr, sc)]
    front = -1
    rear = 0
    visited = [[0] * C for _ in range(R)]
    answer = [[-1] * C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if not arr[i][j]:
                answer[i][j] = 0
                

    
    while front != rear:
        front += 1
        r, c = queue[front]
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if (0 <= nr < R) and (0 <= nc < C) and not visited[nr][nc] and arr[nr][nc]:
                rear += 1
                queue.append((nr, nc))
                visited[nr][nc] += visited[r][c] + 1
                answer[nr][nc] = visited[nr][nc]
    
    return answer

# 목표지점 찾기
def findPoint(arr):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 2:
                return i, j
    return 1001, 1001


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
wall_list = []
# 목표지점 찾기
sr , sc = findPoint(arr)
result = BFS(sr, sc)

result[sr][sc] = 0

for r in result:
    print(*r)