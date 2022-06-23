# 2003_수들의합_문제풀이
# 2022-06-01

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
N_lst = list(map(int, input().split()))

cnt = 0
end = 0
sum_num = 0

# start를 차례대로 증가시키며 반복
for start in range(N):
    # end 이동
    while sum_num < M and end < N:
        sum_num += N_lst[end]
        end += 1
    # 부분 합이 M 일경우 카운트 증가
    if sum_num == M:
        cnt += 1
    sum_num -= N_lst[start]

print(cnt)