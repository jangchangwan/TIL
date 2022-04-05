from sys import stdin
stdin = open('input.txt', 'r')

T = int(stdin.readline())
queue = []
for t in range(T):
    data = stdin.readline().split()
    if data[0] == 'push':
        queue.append(int(data[1]))
    elif data[0] == 'pop':
        if len(queue):
            print(queue.pop(0))
        else:
            print(-1)
    elif data[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    elif data[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif data[0] == 'size':
        print(len(queue))

