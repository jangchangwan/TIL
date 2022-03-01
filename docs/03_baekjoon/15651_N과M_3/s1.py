import sys
sys.stdin = open('input.txt', 'r')


def backT():
    if len(stack) == M:
        print(*stack)
    else:
        for i in range(1, N+1):
            stack.append(i)
            backT()
            stack.pop()


N, M = map(int, input().split())
stack = []
backT()
