"""
문제

지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.
불은 각 지점에서 네 방향으로 확산된다.
지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

입력

입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.
다음 입력으로 R줄동안 각각의 미로 행이 주어진다.
각각의 문자들은 다음을 뜻한다.

#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간
J는 입력에서 하나만 주어진다.

출력
지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.

예제 입력 1 
4 4
####
#JF#
#..#
#..#
예제 출력 1 
3
"""
from collections import deque


def BFS():
    while queue_fire:
        r, c = queue_fire.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 제약조건
            if (0 <= nr < R) and (0 <= nc < C) and not visited_fire[nr][nc] and arr[nr][nc] != "#":
                visited_fire[nr][nc] = visited_fire[r][c] + 1
                queue_fire.append((nr, nc))
    
    while queue_jihoon:
        r, c = queue_jihoon.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 제약 조건
            if (0 <= nr < R) and (0 <= nc < C):
                if not visited_jihoon[nr][nc] and arr[nr][nc] != "#":
                    if not visited_fire[nr][nc] or visited_fire[nr][nc] > visited_jihoon[r][c] + 1:
                        visited_jihoon[nr][nc] = visited_jihoon[r][c] + 1
                        queue_jihoon.append((nr, nc))
            # 탈출 할경우
            else:
                return visited_jihoon[r][c]
    
    # 탈출 불가능
    return "IMPOSSIBLE"

# 입력
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]


visited_fire = [[0] * C for _ in range(R)]    # 불 방문체크
visited_jihoon =  [[0] * C for _ in range(R)] # 지훈이 방문체크

queue_fire = deque()
queue_jihoon = deque()

# 방향
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


for i in range(R):
    for j in range(C):
        if arr[i][j] == "J":
            queue_jihoon.append((i, j))
            visited_jihoon[i][j] = 1
        elif arr[i][j] == "F":
            queue_fire.append((i, j))
            visited_fire[i][j] = 1
            

answer = BFS()
print(answer)