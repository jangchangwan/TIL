import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def binary_search(target, n):
    start = 1
    end = n
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        # 같을경우 횟수를 리턴한다
        cnt += 1
        if mid == target:
            return cnt
        elif mid < target:
            start = mid
        else:
            end = mid
    return None


for t in range(1, T+1):
    N, A, B = map(int, input().split())
    # 이진함수 호출
    a_cnt = binary_search(A, N)
    b_cnt = binary_search(B, N)
    # 결과값 비교
    if a_cnt < b_cnt:
        ans = 'A'
    elif a_cnt > b_cnt:
        ans = 'B'
    else:
        ans = 0

    print('#{} {}'.format(t, ans))