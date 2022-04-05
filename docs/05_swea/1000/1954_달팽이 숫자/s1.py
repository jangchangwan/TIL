import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 달팽이 모양을 담을 빈 리스트를 만든다.
    dal_arr = [[0]*N for _ in range(N)]

    # 달팽이 이동방향 설정 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 초기 위치와 이동방향 설정
    cr = 0
    cc = 0
    k = 0

    # 정렬시킨 1차원 list 를 2차원으로 만든다.
    for i in range(1, N*N+1):
        dal_arr[cr][cc] = i
        cr += dr[k]
        cc += dc[k]
        # 아닐 조건을 넣고 이동방향을 변경한다
        if cr < 0 or cc < 0 or cr >= N or cc >= N or dal_arr[cr][cc] != 0:
            cr -= dr[k]
            cc -= dc[k]

            k = (k+1) % 4

            cr += dr[k]
            cc += dc[k]

    print('#{}'.format(t))
    for arr in dal_arr:
        for i in arr:
            print(i, end=' ')
        print()

