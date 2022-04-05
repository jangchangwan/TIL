import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    day, month, month_3, year = map(int, input().split())
    used_list = list(map(int, input().split()))

    ans = [0]*13
    for i in range(1, 13):
        a = [0, 0, 9999999, 9999999]
        a[0] = ans[i-1] + used_list[i-1] * day
        a[1] = ans[i-1] + month
        if i >= 3:
            a[2] = ans[i-3] + month_3
        if i >= 12:
            a[3] = ans[i-12] + year
        ans[i] = min(a)
    print('#{} {}'.format(tc, ans[12]))