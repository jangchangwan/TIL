# 4866_괄호검사_문제풀이
# 2022-02-22
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    words = input()
    # stack 리스트를 만든다
    stack = list()
    # 조건에 맞지않을 경우 0으로 변환하기위해 1로 설정한다
    ans = 1
    # 문자열을 반복한다
    for word in words:
        # 열린 괄호일 경우 스택에 더해준다
        if word == '(' or word == '{':
            stack += [word]
        # 닫힌 괄호일 경우 동작
        elif word == '}':
            # 스택이 빈 공간이거나 stack top 데이터가 열린괄호가 아닐경우 ans 를 0으로 리턴하고 나온다
            if len(stack) == 0 or stack.pop() != '{':
                ans = 0
                break
        # 닫힌 괄호일 경우 동작
        elif word == ')':
            # 스택이 빈 공간이거나 stack top 데이터가 열린괄호가 아닐경우 ans 를 0으로 리턴하고 나온다
            if len(stack) == 0 or stack.pop() != '(':
                ans = 0
                break
    # 동작이 완료후 스택에 데이터가 남아 있을 경우 ans 를 0으로 리턴
    if len(stack) != 0:
        ans = 0
    print('#{} {}'.format(t, ans))