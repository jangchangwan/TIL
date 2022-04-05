import sys
sys.stdin = open('input.txt', 'r')


# 16진수를 10진수로 변경하는 함수 생성
def trans_num(arr, N):
    for i in range(N):
        if arr[i] == 'A':
            arr[i] = 10
        elif arr[i] == 'B':
            arr[i] = 11
        elif arr[i] == 'C':
            arr[i] = 12
        elif arr[i] == 'D':
            arr[i] = 13
        elif arr[i] == 'E':
            arr[i] = 14
        elif arr[i] == 'F':
            arr[i] = 15


# 내림차순으로 정렬
def my_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    num_lst = list(map(str, input()))

    try_num = N // 4
    # 10진수로 변경
    trans_num(num_lst, N)
    # 결과저장
    result = list()
    for k in range(try_num):
        for i in range(0, N, try_num):
            sum_num = 0
            for j in range(try_num):
                sum_num += (16**(try_num-j-1))*int(num_lst[i+j])
            # 중복 배제
            if sum_num in result:
                continue
            # 아닐경우 포함
            else:
                result.append(sum_num)
        num_lst.append(num_lst.pop(0))
    my_sort(result)
    # K 번째로 큰수 출력
    ans = result[K-1]
    print('#{} {}'.format(t, ans))

