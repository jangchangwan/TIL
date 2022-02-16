import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def binary_search(target, n):
    start = 1
    end = n
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        # 같을경우 값을 찾은 경우이므로 횟수를 리턴한다
        if mid == target:
            return cnt
        # 찾는 값이 높을 경우 start 에 중앙값을 넣는다
        elif mid < target:
            start = mid
        # 찾는 값이 낮을 경우 end 값에 중앙값을 넣는다
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