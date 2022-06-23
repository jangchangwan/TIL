# 11723_집합_문제풀이
# 2022-03-30
# 시간초과
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
S = set()
for _ in range(N):
    temp = list(map(str, input().split()))
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([str(i) for i in range(1, 21)])
        elif temp[0] == 'empty':
            S = set()
    else:
        command, x = temp[0], temp[1]
        if command == 'add':
            S.add(x)
        elif command == 'remove':
            S.discard(x)
        elif command == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
