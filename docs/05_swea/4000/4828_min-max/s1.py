import sys
sys.stdin = open('input.txt', 'r')
# 시행횟수
T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 주어진 num의 제한사항보다 높은 숫자와 낮은숫자를 max , min 으로 할당한다.
    max_num = min_num = nums[0]
    # nums 리스트를 반복시킨다
    for num in nums:
        # min 보다 num 가 작을경우 min 에 num 을 할당한다
        if num < min_num:
            min_num = num
        # max 보다 num 가 작을경우 max 에 num 을 할당한다
        if num > max_num:
            max_num = num

    print('#{} {}'.format(t, max_num-min_num))