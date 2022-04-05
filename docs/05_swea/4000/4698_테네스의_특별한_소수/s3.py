import sys
sys.stdin = open('input.txt', 'r')

N = 1000000
primes = [True] * (N + 1)
for i in range(2, int(N ** (1 / 2)) + 1):
    j = 2
    while i * j <= N:
        primes[i * j] = False
        j += 1

primes[0] = False
primes[1] = False

T = int(input())
for tc in range(1, T + 1):
    D, A, B = map(int, input().split())

    cnt = 0
    for n in range(A, B + 1):
        if primes[n] and str(D) in str(n):
            cnt += 1

    print(f'#{tc} {cnt}')