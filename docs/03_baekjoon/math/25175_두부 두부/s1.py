# 25175_두~~부 두부 두부
# 2022-07-19


N, M, K = map(int, input().split())

answer = ((M - 1) + (K - 3) % N + N) % N + 1
print(answer)