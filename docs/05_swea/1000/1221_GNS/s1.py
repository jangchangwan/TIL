import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    tc, nums = list(input().split())
    nums_list = list(input().split())

    # 값 정렬
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # 횟수 카운터
    cnt_list = [0]*10
    # 각각의 횟수를 카운팅하여 list 에 담는다.
    for n in nums_list:
        for s in range(10):
            if n == num[s]:
                cnt_list[s] += 1
                break
    print(tc)
    for i in range(10):
        for j in range(cnt_list[i]):
            print(num[i], end=' ')
    print()