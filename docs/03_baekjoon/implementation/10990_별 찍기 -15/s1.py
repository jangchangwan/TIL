# 10990_별 찍기 - 15
# 2022-08-07

N = int(input())

if N == 1:
    print("*")
    exit()
for i in range(1, N):
    if i == 1:
        print(' ' * (N-1) + "*")
    print(' ' * (N - i - 1) + '*' + ' ' * (2 * i - 1 ) + '*')