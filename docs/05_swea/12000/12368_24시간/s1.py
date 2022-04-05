import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    now, after = map(int, input().split())

    ans = 0
    if now + after < 24:
        ans = now + after
    else:
        ans = now + after - 24

    print('#{} {}'.format(tc, ans))

