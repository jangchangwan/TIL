# 1247_부호_문제풀이
# 2022-04-17

import sys
sys.stdin = open('input.txt', 'r')

T = 3

for tc in range(T):
    N = int(input())
    total = 0
    for n in range(N):
        total += int(sys.stdin.readline())
    if total == 0:
        print(0)
    elif total > 0:
        print('+')
    else:
        print('-')