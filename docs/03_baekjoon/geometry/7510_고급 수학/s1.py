# 7510_고급 수학_문제풀이
# 2022-05-08

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'Scenario #{t}:')
    if numbers[2]**2 == (numbers[0]**2 + numbers[1]**2):
        print('yes')
    else:
        print('no')
    if t == T:
        break
    else:
        print()