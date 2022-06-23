import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
stack = []
for t in range(T):
    command = sys.stdin.readline().split()
    order = command[0]
    if order == 'push':
        stack += [int(command[1])]

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
