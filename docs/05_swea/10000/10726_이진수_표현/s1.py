# 10726_이진수_표현_문제풀이
# 2022-03-24
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 전부다 받아올 경우 시간초과 발생
    # 검증할 이진수까지만 받아오기
    cnt = 0
    ans = 'ON'
    # 역순으로 받아오기

    if M < 2**(N-1) :
        print('#{} {}'.format(tc, 'OFF'))
        continue
    while M > 0 and cnt < N:
        if M % 2 == 0:
            ans = 'OFF'
            break
        M //= 2
        cnt += 1

    print('#{} {}'.format(tc, ans))

