# 17298_오큰수_문제풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

num_list = list(map(int, input().split()))

ans = [-1] * N
stack = [0]
# 맨 마지막은 무조건 0
for i in range(1, N):
    while stack and num_list[stack[-1]] < num_list[i]:
        ans[stack[-1]] = num_list[i]
        stack.pop()

    stack.append(i)

print(*ans)