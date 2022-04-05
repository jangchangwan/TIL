import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    K, start, end = map(int, input().split())

    num_lst = [0, 0] + [1] * (end - 1)

    ans = list()
    for i in range(2, end+1):
        if num_lst[i]:
            ans.append(i)
            for j in range(2*i, end+1, i):
                num_lst[j] = 0
    cnt = 0
    for num in ans:
        if num >= start:
            break
        else:
            cnt += 1
    ans = ans[cnt:]
    cnt = 0
    for num in ans:
        for t in str(num):
            if t == str(K):
                cnt += 1
                break
    print('#{} {}'.format(tc, cnt))