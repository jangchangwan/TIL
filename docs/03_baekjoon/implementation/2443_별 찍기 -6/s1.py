# 2442_별 찍기 -6
# 2022-07-25


N = int(input())

for i in range(N):
    answer = ' ' * i + '*'*((N - i) * 2 - 1)
    print(answer)