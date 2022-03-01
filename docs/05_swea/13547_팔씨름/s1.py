import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    arr = list(map(str, input()))
    cnt = 0
    ans = 'YES'
    for a in arr:
        if a == 'x':
            cnt += 1

    if cnt > 7:
        ans = 'NO'

    print('#{} {}'.format(tc, ans))