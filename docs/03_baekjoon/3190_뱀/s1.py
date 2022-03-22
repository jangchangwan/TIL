# 3190_뱀_문제풀이
# 2022-03-22

import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # arr 의 크기

apples = int(input()) # 사과 갯수
apple_lst = [] # 사과 담을 리스트
for apple in range(apples):
    row, col = map(int, input().split())
    apple_lst.append((row-1, col-1))

snakes = int(input()) # 뱀 이동
snake_time = [] # 시간
snake_dir = [] # 방향
total = 0 # 총 시간
for snake in range(snakes):
    dis, turn = map(str, input().split())
    snake_time.append(int(dis))
    snake_dir.append(turn)
    total += int(dis)

# 우 -> 하 -> 좌 -> 상
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0 # 초기값
r, c = 0, 0 # 초기값
snake = [(0, 0)]
cnt = 0
for time in range(total):
    # 방향전환
    if time in snake_time:
        if snake_dir[cnt] == 'D':
            d = (d + 1) % 4
            cnt += 1
        else:
            d = (d - 1) % 4
            cnt += 1
    # 이동
    r += dir[d][0]
    c += dir[d][1]

    # 범위를 벗어나는 경우
    if 0 > r or r >= N or c < 0 or c >= N:
        print(time+1)
        break
    # 뱀 몸통과 만나는 경우
    if (r, c) in snake:
        print(time+1)
        break
    # 뱀 머리 추가
    snake.append((r, c))
    # 뱀 꼬리 삭제
    if (r, c) in apple_lst:
        apple_lst.remove((r, c))
    else:
        snake.pop(0)
