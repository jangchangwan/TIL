import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))+[0]
    cnt = 1
    max_cnt = 1
    for i in range(N-1):
        if nums[i] < nums[i+1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print('#{} {}'.format(t, cnt))


