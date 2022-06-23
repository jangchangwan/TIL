# 1920_수-찾기_문제풀이
# 2022-03-30
# 이진탐색
import sys
sys.stdin = open('input.txt', 'r')

# 있는 정수
N = int(input())
N_lst = list(map(int, input().split()))
# 있는지 탐색할 숫자
M = int(input())
M_lst = list(map(int, input().split()))

# 정렬되있는 상태여야 이진탐색이 가능하다
N_lst.sort()

for i in range(M):
    start, end = 0, N-1
    while start <= end:
        ans = 0
        mid = (start + end) // 2
        # 값을 찾을 경우
        if N_lst[mid] == M_lst[i]:
            ans = 1
            break
        elif N_lst[mid] > M_lst[i]:
            end = mid - 1

        elif N_lst[mid] < M_lst[i]:
            start = mid + 1

    print(ans)