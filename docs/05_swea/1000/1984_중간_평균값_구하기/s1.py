import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N_lst = list(map(int, input().split()))
    N_lst.sort()
    N_lst = N_lst[1:9]
    res = sum(N_lst) / 8
    if res - int(res) >= 0.5:
        ans = int(res) + 1
    else:
        ans = int(res)
    print('#{} {}'.format(tc, ans))