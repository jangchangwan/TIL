import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N_lst = list(map(int, input()))

    res = 0
    num = 0
    for n in range(len(N_lst)):
        if n > num and N_lst[n] != 0:
            res += n - num
            num += (n - num)
        num += N_lst[n]
    print('#{} {}'.format(tc, res))