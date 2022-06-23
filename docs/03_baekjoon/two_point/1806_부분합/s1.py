# 1806_부분합_문제풀이
# 2022-06-02
# 시간초과 코드
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, S = map(int, input().split())
N_lst = list(map(int, input().split()))

# 부분합
# 시간 줄이기위해 리스트를 만든다.
total = [0] * (N+1)
total[1] = N_lst[0]
for i in range(2, N+1):
    total[i] = total[i-1] + N_lst[i-1]

start, end = 0, 0
min_S = 100001

while start < N:
    # 합 구하기
    sum_num = total[end+1] - total[start]

    # S보다 클 경우
    if sum_num >= S:
        if end - start + 1 < min_S:
            min_S = end - start + 1
        start += 1
        end = start
    else:
        if end < N-1:
            end += 1
        else:
            break

if min_S != 100001:
    print(min_S)
else:
    print(0)
