import sys
sys.stdin = open('input.txt', 'r')


def backT(s):
    if len(stack) == M:
        print(*stack)
    else:
        for i in range(s, N):
            visited[i] = 1
            stack.append(i)
            backT(i+1)
            visited[i] = 0
            stack.pop()


N, M = map(int, input().split())
stack = []
visited = [0] * N
backT(0)
