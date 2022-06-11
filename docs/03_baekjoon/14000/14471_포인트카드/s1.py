# 14471_포인트 카드
# 2022-06-11

N, M = map(int, input().split())

cost = []
for m in range(M):
    A, B = map(int, input().split())
    if A >= N:
        continue
    cost.append(N-A)

print(sum(cost) - max(cost))