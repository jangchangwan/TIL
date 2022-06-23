import sys
sys.stdin = open('input.txt', 'r')


def back_T():
    global N, M
    if len(stack) == M:
        print(*stack)
    else:
        for i in range(1, N + 1):
            if i in stack:
                continue
            stack.append(i)
            back_T()
            stack.pop()


N, M = map(int, input().split())
stack = list()
back_T()