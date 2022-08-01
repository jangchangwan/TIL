# 2522_별 찍기 12
# 2022-08-01

N = int(input())

for i in range(1, N):
    print((N - i) * ' ' + i * '*')
print('*' * N)
for i in range(1, N):
    print(i * ' ' + (N - i) * '*')