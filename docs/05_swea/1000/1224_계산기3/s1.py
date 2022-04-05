# 1224_계산기3_문제풀이
# 2022-02-24

import sys
sys.stdin = open('input.txt', 'r')


# 후위로 변환
def trans_postfix(arr, N):
    stack = list()
    result = list()
    icp = {'(': 3, '*': 2, '+': 1}
    isp = {'(': 0, '*': 2, '+': 1}
    for i in range(N):
        if arr[i].isdigit():
            result.append(arr[i])

        elif arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while icp[arr[i]] <= isp[stack[-1]]:
                result.append(stack.pop())
            stack.append(arr[i])
    while stack:
        result.append(stack.pop())
    return result


# 계산
def postfix_value(arr):
    stack = list()
    N = len(arr)
    for i in range(N):
        if arr[i] == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
        elif arr[i] == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
        else:
            stack.append(int(arr[i]))

    return stack[-1]


T = 10

for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(str, input()))
    arr = trans_postfix(num_lst, N)
    ans = postfix_value(arr)
    print('#{} {}'.format(t, ans))