# 1223_계산기2_문제풀이
# 2022-02-23

import sys
sys.stdin = open('input.txt', 'r')


# 중위 표기법에서 휘위 표기법으로 변환
def trans_postfix(arr, N):
    temp = []
    stack = [] # 연산자 들어가는 곳
    ip = {'*': 2, '+': 1}
    for i in range(N):
        if arr[i].isdigit(): # 숫자인지 판별
            temp.append(arr[i])
        else:
            # 우선순위가 같거나 작을 경우
            while stack and ip[arr[i]] <= ip[stack[-1]]:
                temp.append(stack.pop())
            stack.append(arr[i])
    # stack 에 남은 연산자 넣기
    while len(stack) != 0:
        temp.append(stack.pop())
    return temp


# 후위표기법 계산
def postfix_value(arr, N):
    ip = ['*', '-']
    stack = []
    num1 = num2 = 0
    for i in range(N):
        if arr[i].isdigit(): # 숫자 인지 판별
            stack.append(int(arr[i]))
        elif arr[i] == '+':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(num1 + num2)
        elif arr[i] == '*':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(num1 * num2)
    return stack[-1]


# 시행횟수
T = 10
for t in range(1, T+1):
    N = int(input())
    prefix_lst = list(map(str, input()))
    postfix_lst = trans_postfix(prefix_lst, N)
    result = postfix_value(postfix_lst, N)
    ans = result
    print('#{} {}'.format(t, ans))