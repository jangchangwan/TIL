# 우선 0으로 이루어진 배열을 만든다음
# 빨강인 부분은 1을 더해주고
# 파랑인 부분은 2로 더해준다
# 3인 부분의 갯수를 카운팅해서 출력

import sys
sys.stdin = open('input.txt', 'r')

# 시행횟수
T = int(input())


for t in range(1, T+1):
    # 색칠 횟수 받아오기
    N = int(input())
    # N만큼 반복
    # 배경
    bg_data = [[0]*10 for i in range(10)]
    # 색칠한 범위
    min_x = min_y = 10
    max_x = max_y = 0

    for n in range(N):
        # N의 데이터 받아오기
        x1, y1, x2, y2, color = list(map(int, input().split()))

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                bg_data[x][y] += color

        # 색칠한 범위 찾기
        if x1 < min_x:
            min_x = x1
        if y1 < min_y:
            min_y = y1
        if x2 > max_x:
            max_x = x2
        if y2 > max_y:
            max_y = y2

    cnt = 0
    # 겹치는 부분찾기
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if bg_data[x][y] == 3:
                cnt += 1
    print('#{} {}'.format(t, cnt))

