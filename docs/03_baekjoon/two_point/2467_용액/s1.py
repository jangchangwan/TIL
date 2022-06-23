# 2467_용액_문제풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt', 'r')

'''
정렬된 상태로 데이터를 준다
투 포인트 알고리즘으로 풀어본다
시간초과
'''
input = sys.stdin.readline
# 입력
N = int(input())
N_lst = list(map(int, input().split()))

min_ans = 20000000000
start, end = 0, 1
ans = [0, 1]
while start < (N-1):
    temp = abs(N_lst[start] + N_lst[end])

    # 0 일경우
    if temp == 0:
        ans[0] = start
        ans[1] = end
        break
    # 값이 작을경우
    elif temp < min_ans:
        min_ans = temp
        ans[0] = start
        ans[1] = end

    if end == (N-1):
        start += 1
        end = start + 1
        continue
    end += 1
print(N_lst[ans[0]], N_lst[ans[1]])