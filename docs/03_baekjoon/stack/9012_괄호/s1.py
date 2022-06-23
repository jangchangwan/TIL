# 9012_괄호_문제풀이
# 2022-02-23
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for n in range(N):
    text = list(input())
    stack = list()
    # text를 반복
    for t in text:
        # stack 이 빈값일 경우 추가
        if len(stack) == 0:
            stack.append(t)
        # 열린 괄호일 경우 추가
        elif t == '(':
            stack.append(t)
        # 닫힌 괄호일 경우
        else:
            # Top 이 열린 괄호일경우만 빼낸다
            if stack[-1] == '(':
                stack.pop()
    # stack 에 아무것도 없을경우 만족
    if len(stack) !=0:
        print('NO')
    else:
        print('YES')