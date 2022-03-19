import sys
sys.stdin = open('input.txt', 'r')


row, col = map(int, input().split())
r, c, dir = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(row)]
# 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 횟수 카운팅
cnt = 0
while True:
    
    check = 0
    # 청소 안했을경우
    if arr[r][c] == 0:
        # 청소한 걸로 변경
        arr[r][c] = 2
        cnt += 1
    # 4방향 탐색
    for _ in range(4):
        # 반시계 방향으로 작동
        dir = (dir + 3) % 4
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 청소 안했을 경우 전진
        if arr[nr][nc] == 0:
            check = 1
            r = nr
            c = nc
            break;
    # 전진 했을경우 아래 코드 무시
    if check == 1:
        continue
    
    r -= dr[dir]
    c -= dc[dir]
    # 후진 했을 때 벽이 있는 경우
    if arr[r][c] == 1:
        break

print(cnt)