import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def binary_search(arr, n, key):
    start = 0
    end = n-1
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        # 같을경우 값을 찾은 경우이므로 횟수를 리턴한다
        if arr[mid] == key:
            return cnt
        # 찾는 값이 높을 경우 start 에 중앙값을 넣는다
        elif arr[mid] < key:
            start = mid + 1
        # 찾는 값이 낮을 경우 end 값에 중앙값을 넣는다
        else:
            end = mid - 1
    return False


for t in range(1, T+1):
    N, A, B = map(int, input().split())
    # 이진함수 호출
    num_lst = list()

    for i in range(1, N+1):
        num_lst.append(i)

    a_cnt = binary_search(num_lst, N, A)
    b_cnt = binary_search(num_lst, N, B)
    print(a_cnt, b_cnt)
    # 결과값 비교
    if a_cnt < b_cnt:
        ans = 'A'
    elif a_cnt > b_cnt:
        ans = 'B'
    else:
        ans = 0

    print('#{} {}'.format(t, ans))