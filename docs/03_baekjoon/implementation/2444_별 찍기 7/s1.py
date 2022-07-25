# 2444_별 찍기 7
# 2022-07-26

N = int(input())
for i in range(1, N):
    print(' '*(N-i) + '*'*(2*i-1))
for i in range(N, 0, -1):
    print(' '*(N-i) + '*'*(2*i-1))