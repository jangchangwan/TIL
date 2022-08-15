# 10995_별찍기
# 2022-08-15


N = int(input())

if N == 1:
    print('*')

else:
    for n in range(N):
        if n % 2 == 0:
            print('* ' * N)
        else:
            print(' *' * N)