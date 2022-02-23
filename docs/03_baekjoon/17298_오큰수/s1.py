# 17298_오큰수_문제풀이
# 2022-02-23
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

num_list = list(map(int, input().split()))

for i in range(N):
    temp = num_list[:]
    stack = []
    while num_list[i] != temp[-1]:
        if num_list[i] < temp[-1]:
            stack.append(temp.pop())
        else:
            temp.pop()
    if stack:
        print(stack[-1], end=' ')
    else:
        print('-1', end=' ')
