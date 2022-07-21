# 2441_별 찍기 -4
# 2022-07-21

N = int(input())

for i in range(N):
    answer = (' ' * i) + ('*' * (N-i))
    print(answer)
