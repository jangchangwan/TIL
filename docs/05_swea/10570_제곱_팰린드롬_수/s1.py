import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    cnt = 0
    for n in range(A, B+1):
        sqrt_n = (n ** 0.5)
        if (sqrt_n % 1 == 0) and (str(n) == str(n)[::-1]):
            new_n = int(sqrt_n)
            if str(new_n) == str(new_n)[::-1]:
                cnt += 1
    print('#{} {}'.format(tc, cnt))