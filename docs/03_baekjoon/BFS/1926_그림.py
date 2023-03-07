# 문제
# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

# 입력
# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
# 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

# 출력
# 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

# 예제 입력 1 
# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1
# 예제 출력 1 
# 4
# 9

# BFS
def BFS(sr, sc):
    global visited

    queue = list()
    queue.append([sr, sc])
    visited[sr][sc] = 1
    front = -1
    rear = 0
    cnt = 1
    
    while front != rear:
        front += 1
        r, c = queue[front]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc] and arr[nr][nc]:
                visited[nr][nc] = 1
                queue.append([nr, nc])
                cnt += 1
                rear += 1
    return cnt


# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 변수 초기화
visited = [[0] * M for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
count = 0 # 그림 갯수
max_value = 0 # 최대 크기

# 동작
for i in range(N):
    for j in range(M):
        # 그림 발견시 동작 & 체크한 그림은 무시
        if arr[i][j] == 1 and visited[i][j] == 0:
            value = BFS(i, j)
            if value > max_value:
                max_value = value
            count += 1

# 출력
print(count)
print(max_value)