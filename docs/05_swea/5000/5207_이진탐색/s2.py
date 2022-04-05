T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    N_lst = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))
    N_lst.sort()

    cnt = 0
    for n in N_lst:
        if n in M_lst:
            cnt += 1
    print('#{} {}'.format(tc, cnt))