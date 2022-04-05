T = int(input())

for t in range(1,T+1):
    N_lst = list(map(int, input().split()))
    ans = 0
    for n in N_lst:
        if n % 2:
            ans += n
    print('#{} {}'.format(t, ans))