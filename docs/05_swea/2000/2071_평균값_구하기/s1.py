T = int(input())

for t in range(1, T+1):
    num_lst = list(map(int, input().split()))
    total = 0
    for n in num_lst:
        total += n

    ave = total / 10
    if (ave - int(ave)) < 0.5:
        ans = int(ave)
    else:
        ans = int(ave) + 1
    print('#{} {}'.format(t, ans))
