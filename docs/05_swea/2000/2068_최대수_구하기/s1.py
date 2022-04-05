T = int(input())

for t in range(1,T+1):
    num_lst = list(map(int,input().split()))
    ans = 0
    for n in num_lst:
        if n > ans:
            ans = n
    print('#{} {}'.format(t, ans))