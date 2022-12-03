# 10103_주사위게임
# 시뮬레이션

T = int(input())

A, B = 100, 100
for tc in range(T):
    N, M = map(int, input().split())

    if N > M:
        A -= N
    elif N < M:
        B -= M

print(B)
print(A)