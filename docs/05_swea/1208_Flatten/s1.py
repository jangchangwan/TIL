import sys
sys.stdin = open('input.txt', 'r')

T = 10
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 1~100까지 숫자이므로
    cnt_nums = [0]*101
    # 각 숫자가 카운팅하기
    for num in nums:
        cnt_nums[num] += 1
    # N 만큼 반복하게한다
    max_result = 100
    min_result = 1
    for n in range(N):
        # cnt_nums == 0 인경우 제외한다.
        for num in range(max_result, 0, -1):
            if cnt_nums[num] != 0:
                # 상자 위치 변경
                cnt_nums[num] -= 1
                cnt_nums[num-1] += 1
                # 반복횟수 줄이기
                max_result = num
                break
        for num in range(min_result, 101):
            if cnt_nums[num] != 0:
                # 상자 위치 변경
                cnt_nums[num] -= 1
                cnt_nums[num+1] += 1
                # 반복횟수 줄이기
                min_result = num
                break
        # 마지막 작업이 끝난후 값을 구해야하므로 한번더 동작시킨다
        for num in range(max_result, 0, -1):
            if cnt_nums[num] != 0:
                max_result = num
                break
        for num in range(min_result, 101):
            if cnt_nums[num] != 0:
                min_result = num
                break
        # 가장 큰값의 cnt_nums 값을 -1한다
        # 가장 작은값의 cnt_nums 값을 +1한다
    print('#{} {}'.format(t, max_result-min_result))
