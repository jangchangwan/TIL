import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())
    text = input()

    stack = []
    open_lst = {'(': 1, '{': 2, '[': 3}
    close_lst = {')': 1, '}': 2, ']': 3}
    ans = 1
    for i in range(N):
        if text[i] in open_lst.keys():
            stack.append(text[i])
        elif text[i] in close_lst.keys():
            temp = stack.pop()
            if open_lst[temp] != close_lst[text[i]]:
                ans = 0
                break
    if len(stack) != 0:
        ans = 0

    print('#{} {}'.format(tc, ans))