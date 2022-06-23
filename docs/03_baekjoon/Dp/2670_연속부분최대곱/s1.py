# 2670_연속부분최대곱
# 2022-06-20

N = int(input())

N_lst = [float(input()) for _ in range(N)]


for n in range(1, N):
    N_lst[n] = max(N_lst[n], N_lst[n-1] * N_lst[n])

answer = max(N_lst)
print(f'{answer:.3f}')