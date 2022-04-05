import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # 입력값 받아오기
    K, N, M = map(int, input().split())
    m_list = list(map(int, input().split()))
    # 현재위치,횟수 변수 할당
    cnt = 0
    location = 0
    # 도착할떄 까지 반복해라
    while location+K < N:
        # 그리드 기법(?) 현재위치에서 가장 멀리 가기!
        # 최대거리에서부터 1씩 감소
        for i in range(K, 0, -1):
            # 이동거리 + 현재위치에 정류장이 있는경우 동작
            if i+location in m_list:
                # 현재위치에 이동거리만큼 더해준다
                location += i
                cnt += 1
                # for 문을 빠져나온다.
                break
        # 이동거리보다 정류장이 멀경우 0으로 출력        
        else:
            cnt = 0
            break
        # print('location : ', location)
        # print('cnt : ', cnt)
    print('#{} {}'.format(t, cnt))