# 1654_랜선-자르기_문제풀이
# 2022-03-30
# 이분탐색
import sys
sys.stdin = open('input.txt', 'r')

K, N = map(int, input().split())

K_lst = [int(input()) for _ in range(K)]

start = 1
end = max(K_lst)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for k in K_lst:
        cnt += k // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)