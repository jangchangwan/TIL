# 입력
N = int(input())
M = int(input())

# 변수 초기화
arr = [[0]*N for _ in range(N)] # 빈배열
dir = 0 # 초기방향
target = int(N**2) - 1 # 초기 시작값
arr[0][0] = int(N**2) # 첫 값

# 아래 오른쪽 위 왼쪽
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

r, c = 0, 0 # 위치
mr, mc = 0, 0 # 찾고자하는 값 위치 초기값
# 배열 만들기
while target:
    nr = r + dr[dir]
    nc = c + dc[dir]
    if (0 <= nr < N) and (0 <= nc < N) and arr[nr][nc] == 0:
        arr[nr][nc] = target
        target -= 1
        r = nr
        c = nc
    # 범위를 벗어나는 경우 방향전환
    else:
        dir = (dir + 1) % 4

# 타켓 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == M:
            mr = i
            mc = j        

# 출력
for a in arr:
    print(*a)
print(mr+1, mc+1)
