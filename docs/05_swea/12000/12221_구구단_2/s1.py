import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    if A > 9 or B > 9:
        ans = -1
    else:
        ans = A * B
    print('#{} {}'.format(tc, ans))