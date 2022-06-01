# 2230_수 고르기_문제풀이
# 2022-06-01

import sys
sys.stdin = open('input.txt', 'r')

# 입력
N, M = map(int, input().split())
N_lst = [int(input()) for _ in range(N)]

# 변수 설정
N_lst.sort()
min_M = 2000000000
start, end = 0, 0
while start < N:
    temp = abs(N_lst[end] - N_lst[start])

    if temp == M:
        min_M = M
        break
    elif temp > M:
        min_M = min(min_M, temp)
        # 뒤에는 더이상 검사할 필요 X
        start += 1
        end = start
        continue
    # end 이동
    end += 1
    # 재반복
    if end == N:
        start += 1
        end = start

print(min_M)