import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    total = 0
    for n in range(N):
        now_D = D*(1 + n *(L * 0.01))
        total += now_D
    ans = int(total)
    print(f'#{tc} {ans}')