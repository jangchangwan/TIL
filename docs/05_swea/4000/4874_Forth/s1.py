# 4874_Forth_문제풀이
# 2022-02-24
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def postfix_value(arr):
    stack = list()
    i = 0
    # 연산자 리스트
    ip = ['+', '-', '*', '/']
    # . 을 만날 경우 종료
    while arr[i] != '.' and i < len(arr):
        # 숫자일 경우
        if arr[i].isdigit():
            stack.append(int(arr[i]))
        # stack 길이가 2이상 이고 연산자일 경우
        elif len(stack) > 1 and arr[i] in ip:
            num_1 = stack.pop()
            num_2 = stack.pop()
            # + 연산자일경우
            if arr[i] == '+':
                stack.append(num_2 + num_1)
            # - 연산자일경우
            elif arr[i] == '-':
                stack.append(num_2 - num_1)
            # * 연산자일경우
            elif arr[i] == '*':
                stack.append(num_2 * num_1)
            # / 연산자일경우
            elif arr[i] == '/':
                stack.append(num_2 // num_1)
        # 아닐경우 error 동작이며 반복문을 빠져나온다
        else:
            return 'error'
        i += 1
    if len(stack) == 1:
        return stack[-1]
    else:
        return 'error'


for t in range(1, T+1):
    num_list = list(input().split())
    ans = postfix_value(num_list)
    print('#{} {}'.format(t, ans))