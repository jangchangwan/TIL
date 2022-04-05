import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, Pd, Pg = map(int, input().split())
    ans = 'Broken'
    if Pg == 0 and Pd != 0:
        ans = 'Broken'
    elif Pg == 100 and Pd != 100:
        ans = 'Broken'
    else:
        for n in range(1, N+1):
            if (n * Pd / 100) == (n * Pd // 100):
                ans = 'Possible'
                break

    print('#{} {}'.format(tc, ans))