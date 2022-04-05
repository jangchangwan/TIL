import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
# m, n, h 입력
m, n, h = map(int, input().split(" "))
# 상자에 담긴 토마토의 정보 ( N개의 줄이 H번 반복되며 들어옴. 처음이 맨 밑에 층)
boxStack = []
for i in range(h): # h개의 층의 박스를 입력
    boxStack.append([list(map(int, input().split(" "))) for _ in range(n)])

# 익은 토마토를 전부 큐에 삽입. ( 익은 토마토 인접 토마토들이 다 같이 익어가야하기 때문. )
ripeTomato = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxStack[i][j][k] == 1:
                ripeTomato.append((i, j, k))

# 토마토가 다 익히기 위한 bfs 알고리즘
dh = [1, -1, 0, 0, 0, 0] # 상, 하, 우, 좌, 앞, 뒤
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
def bfs(ripeTomato, boxStack):
    while ripeTomato:
        height, row , col = ripeTomato.popleft()
        for i in range(6):
            adjHeight, adjRow, adjCol = height+dh[i], row+dx[i], col+dy[i]
            if 0<=adjHeight<h and 0<=adjRow<n and 0<=adjCol<m and boxStack[adjHeight][adjRow][adjCol] == 0:
                # 범위안에 존재하고 익지 않은 토마토를 발견했을떄
                boxStack[adjHeight][adjRow][adjCol] = boxStack[height][row][col] + 1
                ripeTomato.append((adjHeight, adjRow, adjCol))

bfs(ripeTomato, boxStack) # 토마토 익히기

# 최소일수 구하기
zeroCheck = False
result = 0
for i in range(h):
    for j in boxStack[i]:
        if 0 in j:
            zeroCheck = True
            break
        result = max(result, max(j))

if zeroCheck:
    print("-1")
else:
    print(result-1)