import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = input()+'0'
    cnt_list = list()
    cnt = 0
    for i in range(N+1):

        if nums[i] == '1':
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0
    max_cnt = 0
    for c in cnt_list:
        if c > max_cnt:
            max_cnt = c
    ans = max_cnt
    print('#{} {}'.format(t, ans))