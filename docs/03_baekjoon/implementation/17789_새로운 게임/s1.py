# 17780 새로운 게임
# 2022-06-28
import sys

def go(num):
    r, c, z = chess[num] # 움직일 체스말의 정보 반환

    # 해당 말이 다른 말에 올려져있는 경우
    if num != stack[r][c][0]:
        return 0

    nr = r + dr[z]
    nc = c + dc[z]

    # 파란색 칸이거나 범위에 벗어나는 경우
    if not (0 <= nr < N) or not(0 <= nc < N) or arr[nr][nc] == 2:
        # 상 하
        if 0 <= z <= 1:
            nz = (z+1) % 2
        # 좌 우
        else:
            nz = (z-1) % 2 + 2

        # 방향 바꿈
        chess[num][2] = nz
        nr = r + dr[nz]
        nc = c + dc[nz]

        # 바꿔서 이동하려는 칸이 파란색 판인 경우
        if not (0 <= nr < N) or not(0 <= nc < N) or arr[nr][nc] == 2:
            return 0

    chess_set = [] # 이동할 체스 묶음
    chess_set.extend(stack[r][c])
    stack[r][c] = [] # 해당 좌표 초기화


    # 빨강색인 경우 순서를 반대로 바꾼다
    if arr[nr][nc] == 1:
        chess_set = chess_set[-1::-1]


    for i in chess_set:
        stack[nr][nc].append(i) # 다음 위치에 쌓인 체스말 정보 입력
        chess[i][:2] = [nr, nc] # 체스말 위치 정보 갱신

    # 4개의 말이 모두 쌓인 경우 1을 return
    if len(stack[nr][nc]) >= 4:
        return 1
    return 0


# 방향
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# 입력
N, K = map(int, input().split()) # N : 체스판의 크기, K : 말의 개수
arr = [list(map(int, input().split())) for _ in range(N)]

stack = [[[] for _ in range(N)] for _ in range(N)]
chess = [0 for _ in range(K)]


for i in range(K):
    r, c, dir = map(int, input().split()) # 행, 열, 이동방향
    stack[r - 1][c - 1].append(i)
    chess[i] = [r - 1, c - 1, dir - 1] # 현재 체스말의 위치(행,열)와 이동방향

cnt = 1
while cnt <= 1000:
    # 체스 말 순서대로
    for i in range(K):
        flag = go(i)
        if flag:
            print(cnt)
            sys.exit()
    # 아직 이동중이라면 cnt 증가 후 이동 반복
    cnt += 1
# 못찾은 경우
print(-1)