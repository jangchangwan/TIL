import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    min_ans = 700000
    for i in range(7):
        N_lst.append(N_lst.pop(0))

        ans = cnt = j = 0
        while cnt != N:
            if N_lst[j % 7] == 1:
                cnt += 1
            ans += 1
            j += 1
        if ans < min_ans:
            min_ans = ans

    print('#{} {}'.format(tc, min_ans))