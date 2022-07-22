# 2442_별 찍기 -5
# 2022-07-22

N = int(input())

for i in range(1, N+1):
    answer = ' ' * (N - i) + '*' * (2 * (i - 1) + 1)
    print(answer)