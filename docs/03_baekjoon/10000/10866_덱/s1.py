# 10866_덱_문제풀이
# 2022-04-07

# deque를 사용한 문제풀이
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())
dq = deque()
for tc in range(T):
    command = sys.stdin.readline().split()

    if command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
