import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 점1과 점2의 거리 구하기
    xy_distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    r_abs = ((r1 - r2)**2)**0.5
    # print('r_abs : ', r_abs)
    # print('xy_distance : ', xy_distance)
    # 동일할 경우 개수는 무한대이므로 -1로 리턴
    if xy_distance == 0 and r1 == r2:
        ans = -1
    # 외접, 내접하는 경우
    elif xy_distance == r1 + r2 or xy_distance == r_abs:
        ans = 1
    # 두원이 두점에서 만나는 경우
    elif r1 + r2 > xy_distance > r_abs:
        ans = 2
    else:
        ans = 0

    print(ans)