# 우선 0으로 이루어진 배열을 만든다음
# 빨강인 부분은 1을 더해주고
# 파랑인 부분은 2로 더해준다
# 3인 부분의 갯수를 카운팅해서 출력
from pprint import pprint
# 시행횟수
T = int(input())


#print(bg_data)

for t in range(1,T+1):
    # 색칠 횟수 받아오기
    N = int(input())
    # N만큼 반복
    # 배경
    bg_data = [[0]*10 for i in range(10)]
    #색칠한 범위
    min_location = [10,10]
    max_location = [0,0]

    for n in range(N):
        # N의 데이터 받아오기
        N_data = list(map(int,input().split()))
        # 색칠공간과 컬러 분리
        spaces = N_data[0:4]
        color = N_data[4]
        # 빨강일경우 배경에 1씩더하기
        if color == 1:
            for x in range(spaces[0],spaces[2]+1):
                for y in range(spaces[1],spaces[3]+1):
                    bg_data[x][y] += 1
        # 블루일 경우 배경에 2씩더하기
        elif color == 2:
            for x in range(spaces[0],spaces[2]+1):
                for y in range(spaces[1],spaces[3]+1):
                    bg_data[x][y] += 2
        # 둘다 아닌경우 무시
        else :
            continue
        # 색칠한 범위 찾기
        if spaces[0] < min_location[0]:
            min_location[0] = spaces[0]
        if spaces[1] < min_location[1]:
            min_location[1] = spaces[1]
        if spaces[2] > max_location[0]:
            max_location[0] = spaces[2]
        if spaces[3] > max_location[1]:
            max_location[1] = spaces[3]
        # pprint(bg_data)
        # print('min_location :',min_location)
        # print('max_location :',max_location)
    cnt = 0

    for x in range(min_location[0],max_location[0]+1):
        for y in range(min_location[1],max_location[1]+1):
            if bg_data[x][y] == 3:
                cnt += 1
    print('#{} {}'.format(t,cnt))

