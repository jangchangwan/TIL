# 2230_수 고르기_문제풀이
# 2022-06-01

import sys
sys.stdin = open('input.txt', 'r')

# 입력
N, M = map(int, input().split())
N_lst = [int(input()) for _ in range(N)]
N_lst.sort()
# 변수 설정
min_M = 10000000000
for start in range(N):
    end = start
    temp = 0
    # end 이동
    while temp < M and end < N:
        temp = abs(N_lst[start] - N_lst[end])
        end += 1
    # 차이가 M 일 경우 종료
    if temp == M:
        min_M = M
        break
    elif temp > M:
        min_M = min(temp, min_M)

print(min_M)
