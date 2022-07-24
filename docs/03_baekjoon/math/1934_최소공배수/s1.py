# 1934_최소공배수
# 2022-07-24


def Euclidean(a, b):
    r = b % a
    if r == 0:
        return a
    return Euclidean(r, a)


T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    C = Euclidean(A, B)
    answer = A * B / C
    print(int(answer))