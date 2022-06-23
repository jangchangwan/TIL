# 17298_오큰수_문제풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')


N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    temp = num_list[i+1:][::-1]
    stack = []
    while temp:
        if num_list[i] < temp[-1]:
            stack = temp.pop()
            break
        else:
            temp.pop()
    if stack:
        print(stack, end=' ')
    else:
        print('-1', end=' ')