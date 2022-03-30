# 1874_스택_수열_문제풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
# 오름차순으로 뽑아오기
num_list = [x for x in range(1, N+1)]

stack = list()
temp = num_list[::-1]
result = list()
ans = 1
for i in range(N):
    num = int(input())
    while True:
        if len(stack) == 0:
            stack.append(temp.pop())
            result += ['+']
        elif num == stack[-1]:
            stack.pop()
            result += ['-']
            break
        elif num != stack[-1]:
            if not temp:
                result = ['NO']
                ans = 0
                break
            else:
                stack.append(temp.pop())
                result += ['+']
    if ans == 0:
        break
for r in result:
    print(r)