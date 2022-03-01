import sys
sys.stdin = open('input.txt', 'r')


def back_T(start):
    if len(stack) == M:
        print(*stack)
    else:
        for i in range(start, N+1):
            stack.append(i)
            back_T(i)
            stack.pop()


N, M = map(int, input().split())
stack = []
back_T(1)
