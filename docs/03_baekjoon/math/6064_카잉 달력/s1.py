# 6064_카잉 달력
# 2022-08-14

def solution():
    global M, N, x, y
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


T = int(input())

for tc in range(T):
    M, N, x, y = map(int, input().split())
    print(solution())
