import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    N_lst = [1] + list(map(int, input().split())) + [1]
    i = 0
    cnt = 0
    while i+K <= N:
        s_i = i
        for k in range(K, 0, -1):
            if (0 <= i+k < N) and N_lst[i+k] == 1:
                i += k
                break

        if s_i == i:
            i += K
            cnt += 1
    print('#{} {}'.format(tc, cnt))

