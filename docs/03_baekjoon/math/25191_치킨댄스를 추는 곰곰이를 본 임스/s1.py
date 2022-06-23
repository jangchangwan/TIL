# 25191_치킨댄스를 추는 곰곰이를 본 임스
# 2022-06-19

N = int(input())
A, B = map(int, input().split())

ans = A // 2 + B


if ans > N:
    print(N)
else:
    print(ans)