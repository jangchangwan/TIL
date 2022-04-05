import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    s = [0] + [1 for i in range(13)]
    d = s[:]
    h = s[:]
    c = s[:]

    N_lst = list(map(str, input()))

    for i in range(0, len(N_lst), 3):
        num = int(N_lst[i + 1] + N_lst[i + 2])
        if N_lst[i] == 'S':
            s[num] -= 1
        elif N_lst[i] == 'D':
            d[num] -= 1
        elif N_lst[i] == 'H':
            h[num] -= 1
        else:
            c[num] -= 1

    cnt = [0, 0, 0, 0]
    for i in range(1, 14):
        if s[i] < 0 or d[i] < 0 or h[i] < 0 or c[i] < 0 :
            cnt = ['ERROR']
            break
        if s[i] == 1:
            cnt[0] += 1
        if d[i] == 1:
            cnt[1] += 1
        if h[i] == 1:
            cnt[2] += 1
        if c[i] == 1:
            cnt[3] += 1

    print('#{}'.format(tc), end=' ')
    for i in range(len(cnt)):
        if i == len(cnt)-1:
            print(cnt[i])
        else:
            print(cnt[i], end=' ')