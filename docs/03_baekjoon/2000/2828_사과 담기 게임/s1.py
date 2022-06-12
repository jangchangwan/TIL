# 2828_사과담기게임
# 2022-06-11

N, M = map(int, input().split())
J = int(input())
apples = list(int(input()) for _ in range(J))

total = 0
start = 1
end = M
for i in range(J):
    if end >= apples[i] and start <= apples[i]:
        continue

    elif end < apples[i]:
        total += apples[i] - end
        end = apples[i]
        start = apples[i] - (M - 1)

    elif start > apples[i]:
        total += start - apples[i]
        start = apples[i]
        end = apples[i] + (M - 1)

print(total)