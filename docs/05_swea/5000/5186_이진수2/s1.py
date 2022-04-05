# 5186_이진수2_문제풀이
# 2022-03-24

import sys
sys.stdin = open('input.txt', 'r')

def find_floating_point(n):
    global N
    ans = ''
    cnt = 1
    # 12번까지 동작
    while cnt < 13:
        r = N // (2 ** (-cnt)) # 나누어 떨어지는 몫은 1 또는 0 이다
        N = N - r * (2 ** (-cnt))
        print(ans)
        ans += str(int(r)) # 더해주기
        if N == 0:
            return ans
        cnt += 1
    # 답을 찾지 못했을 경우
    return 'overflow'


T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = find_floating_point(N)
    print('#{} {}'.format(tc, ans))




