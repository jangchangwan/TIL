# 11723_집합_문제풀이
# 2022-03-30
# 비트마스킹

import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
S = 0
for _ in range(N):
    temp = sys.stdin.readline().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            S = (1 << 21) - 1
        elif temp[0] == 'empty':
            S = 0
    else:
        command, x = temp[0], int(temp[1])
        if command == 'add':
            S |= (1 << x)
        elif command == 'remove':
            S &= ~(1 << x)
        elif command == 'check':
            if S & (1 << x):
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            S ^= (1 << x)