# 시행횟수 받아오기
T = int(input())
# 반복
for t in range(1,T+1):
    # 입력값 받아도기
    distance , end_point, via_points = map(int,input().split())
    via_point_list = list(map(int,input().split()))
    
    # print(distance , end_point, via_points)
    # print(via_point_list)
    # 변수 설정 : 현재위치, 이동횟수
    location = 0
    cnt = 0
    # distance를 더하는 이유
    # 더하지않을경우 마지막 동작에서 else문으로 빠저나옴
    while location+distance < end_point :
        # 제일 멀리있는 정류장을 찾는다
        for via_point in range(distance,0,-1):
            if (location+via_point) in via_point_list:
                # 있을경우 현재위치에 via_point를 더해준다
                location += via_point
                #이동횟수 1를 더한후 빠저나온다
                cnt += 1
                break
        else:
            cnt = 0
            break
    # 이동거리내에 정류점이 있을경우 제일 먼곳으로 간다.
    # cnt += 1한다
    # 없을경우 0으로 리턴
    print('#{} {}'.format(t,cnt))