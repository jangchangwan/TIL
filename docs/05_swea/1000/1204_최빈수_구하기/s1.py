import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    _ = input()
    num_lst = list(map(int, input().split()))
    cnt_lst = [0] * 101
    for n in num_lst:
        cnt_lst[n] += 1
    max_num = 0
    max_cnt = 0
    for i in range(1, len(cnt_lst)):

        if cnt_lst[i] >= max_cnt:
            max_cnt = cnt_lst[i]
            max_num = i
    ans = max_num
    print('#{} {}'.format(tc, ans))