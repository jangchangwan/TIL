import sys

sys.stdin = open('input.txt', 'r')


def sort_list(a, n):
    for i in range(n-1):
        for j in range(1, n-i):
            if a[i] > a[i + j]:
                a[i], a[i + j] = a[i + j], a[i]
    return a


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    # 정렬하기
    sort_nums = sort_list(num_list, N)
    # 특별한 정렬을 담을 리스트 생성
    ans_list = list()
    cnt = 1
    # 리스트가 10개가 찰동안 작동한다!
    while len(ans_list) != 10:
        # 큰 값 출력
        if cnt % 2:
            ans_list.append(sort_nums.pop())
        # 작은 값 출력
        else:
            ans_list.append(sort_nums.pop(0))
        cnt += 1

    print('#{}'.format(t), end=' ')
    for ans in ans_list:
        print(ans, end=' ')
    print()
