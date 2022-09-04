# 1333_부재중 전화
# 2022-08-30

N, L, D = map(int, input().split())

check = [0] * (N * L + 5 * (N - 1))
for i in range(N):
    S = (L + 5) * i
    for j in range(S, S + L):
        check[j] = True

answer = 0
while answer < len(check):
    if not check[answer]:
        break
    answer += D
print(answer)
