# 2473_세 용액_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 입력
N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()
min_ans = 30000000000
ans = [0, 0, 0]

for start in range(N-2):
    mid, end = start+1, N-1

    while mid < end:
        sum_num = N_lst[start] + N_lst[mid] + N_lst[end]

        if abs(sum_num) < min_ans:
            ans[0] = N_lst[start]
            ans[1] = N_lst[mid]
            ans[2] = N_lst[end]
            min_ans = abs(sum_num)

        if sum_num == 0:
            break
        elif sum_num < 0:
            mid += 1
        else:
            end -= 1

print(*ans)