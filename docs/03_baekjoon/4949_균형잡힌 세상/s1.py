# 4949_균형잡힌_세상_문제풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')

while True:
    data = input()
    stack = []
    # 종료 조건
    if data == '.':
        break

    text = list(data)
    ans = 'yes'
    i = 0
    while i < len(text):
        # 열린 괄호 일 경우 더해준다
        if text[i] == '(' or text[i] == '[':
            stack.append(text[i])
        elif text[i] == ')':
            # stack 안에 있고 top 이 열린괄호인 경우
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'no'
                break
        elif text[i] == ']':
            # stack 안에 있고 top 이 열린괄호인 경우
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ans = 'no'
                break
        i += 1
    # stack 이 비어있거나 ans 가 yes 인경우
    if ans == 'yes' and not stack:
        print('yes')
    else:
        print('no')