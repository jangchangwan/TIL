import sys
sys.stdin = open('input.txt', 'r')


def backT(start):
    if len(stack) == M:
        print(*stack)
    else:
        for i in range(start, N+1):
            if i in stack:
                continue
            stack.append(i)
            backT(i+1)
            stack.pop()


N, M = map(int, input().split())
stack = list()
visited = [[]]
backT(1)
